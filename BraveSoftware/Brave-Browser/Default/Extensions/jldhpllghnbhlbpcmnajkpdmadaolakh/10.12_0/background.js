const DOMAIN = 'todoist.com'
const QUICK_ADD_WIDTH = 550
const QUICK_ADD_HEIGHT = 380
const QUICK_ADD_URL = 'https://todoist.com/add?'

const DOIST_HEADERS_PLATFORM_KEY = 'Doist-Platform'
const DOIST_HEADERS_WRAPPER_VERSION_KEY = 'Doist-WrapperVersion'

const TODOIST_CLIENT_VERSION_WRAPPER = 'TodoistForChromium'

const TIMEOUT_1_MIN = 15 * 60 * 1000

let TIMEOUT_WS_CONNECT = null
let WS_SOCKET = null
let USER_TOKEN = null

/*
 * For fetching the current location and title
 */
let CURRENT_LOCATION = {
    location: '',
    title: '',
}

function getCurrentLocationAndTitle() {
    return CURRENT_LOCATION
}

setInterval(function () {
    browserApi.withActiveTab((tab) => {
        CURRENT_LOCATION.location = tab.url
        CURRENT_LOCATION.title = tab.title
    })
}, 200)

/*
 * For remebering the last viewed iframe URL
 */
let FRAME_SRC = null
function setFrameLocation(url) {
    if (url) {
        FRAME_SRC = url
        if (window.localStorage) localStorage['frame_src'] = url
    }
}

function getFrameLocation() {
    let saved = null

    if (window.localStorage) saved = window.localStorage['frame_src']

    if (saved) return saved
    else return FRAME_SRC
}

function getSession() {
    return window.localStorage
}

/*
 * Option management
 */

const ExtensionOptions = {
    withDueToday: false,
}

function applyExtensionOptions(options) {
    ExtensionOptions.withDueToday = options.withDueToday
}

browserApi.getExtensionOptions(applyExtensionOptions)

browserApi.addExtensionOptionsChangedListener(() =>
    browserApi.getExtensionOptions(applyExtensionOptions),
)

function pad(num) {
    if (num < 10) {
        return '0' + num
    }
    return num
}

/*
 * iso date string format YYYY-MM-DD
 */
function isoDateOnly(date) {
    return date.getFullYear() + '-' + pad(date.getMonth() + 1) + '-' + pad(date.getDate())
}

/*
 * Context menu adding
 */
function getQuickAddPosition(win) {
    if (win) {
        const top = win.height / 2 - QUICK_ADD_HEIGHT / 2 + win.top
        const left = win.width / 2 - QUICK_ADD_WIDTH / 2 + win.left
        return [top, left]
    } else {
        const top = screen.height / 2 - QUICK_ADD_HEIGHT / 2
        const left = screen.width / 2 - QUICK_ADD_WIDTH / 2
        return [top, left]
    }
}

function showTodoistQuickAdd(content, top, left) {
    let urlParms = `content=${encodeURIComponent(content)}&view_mode=window`
    if (ExtensionOptions.withDueToday) {
        urlParms += '&date=today'
    }
    browserApi.windowCreate(
        {
            url: QUICK_ADD_URL + urlParms,
            type: 'popup',
            width: QUICK_ADD_WIDTH,
            height: QUICK_ADD_HEIGHT,
            top: Math.round(top),
            left: Math.round(left),
        },
        true,
    )
}

function addTabAsTask(contentToAdd) {
    browserApi.windowGetCurrent(function (win) {
        const [top, left] = getQuickAddPosition(win)
        showTodoistQuickAdd(contentToAdd, top, left)
    })
}

function addToTodoistFromMenu(ev, tab) {
    const url = ev.pageUrl

    let text = (tab && tab.title) || ''
    if (ev.selectionText) {
        text = ev.selectionText
    }

    let contentToAdd = url

    if (ev.linkUrl === text) {
        contentToAdd = ev.linkUrl
    } else if (text.length > 0) {
        text = text.replace(/\(/g, '[').replace(/\)/g, ']')
        text = text.replace(/https?:\/\/[^\s]+/g, '')
        contentToAdd = `[${text}](${url})`
    }

    addTabAsTask(contentToAdd)
}

browserApi.contextMenuCreate(
    {
        title: browserApi.getLocalizedMessage('addToTodoist'),
        contexts: ['page', 'selection', 'link'],
    },
    addToTodoistFromMenu,
)

function addToTodoistCommand() {
    browserApi.tabsQuery(
        {
            active: true,
            lastFocusedWindow: true,
        },
        function (tabs) {
            if (tabs.length > 0) {
                const tab = tabs[0]
                addToTodoistFromMenu({ pageUrl: tab.url }, tab)
            } else {
                const [top, left] = getQuickAddPosition()
                showTodoistQuickAdd('', top, left)
            }
        },
    )
}

browserApi.addCommandListener(function (command) {
    switch (command) {
        case 'add-to-todoist':
            addToTodoistCommand()
            break
        default:
            console.warn('Unrecognized command:', command)
    }
})

function addDoistVersionHeader(currentHeaders) {
    const { version } = browserApi.getRuntimeApi().getManifest()

    const wrapperVersionHeader = {
        name: DOIST_HEADERS_WRAPPER_VERSION_KEY,
        value: `${TODOIST_CLIENT_VERSION_WRAPPER}-Chrome/${version}`,
    }

    // We overwrite any previous headers with the same name.
    return currentHeaders
        .filter((x) => x.name.toLowerCase() !== DOIST_HEADERS_WRAPPER_VERSION_KEY)
        .concat([wrapperVersionHeader])
}

function addDoistPlatformHeader(currentHeaders) {
    const platformHeader = {
        name: DOIST_HEADERS_PLATFORM_KEY,
        value: 'Chrome',
    }

    // We overwrite any previous headers with the same name.
    return currentHeaders
        .filter((x) => x.name.toLowerCase() !== DOIST_HEADERS_PLATFORM_KEY)
        .concat([platformHeader])
}

if (chrome.declarativeNetRequest != undefined) {
    const { version } = browserApi.getRuntimeApi().getManifest()

    chrome.declarativeNetRequest.updateSessionRules(
        {
            removeRuleIds: [1],
            addRules: [
                {
                    id: 1,
                    priority: 1,
                    action: {
                        type: 'modifyHeaders',
                        requestHeaders: [
                            {
                                header: DOIST_HEADERS_PLATFORM_KEY,
                                operation: 'set',
                                value: 'Chrome',
                            },
                            {
                                header: DOIST_HEADERS_WRAPPER_VERSION_KEY,
                                operation: 'set',
                                value: `${TODOIST_CLIENT_VERSION_WRAPPER}-Chrome/${version}`,
                            },
                        ],
                    },
                    condition: {
                        urlFilter: '||todoist.com/*',
                        tabIds: [chrome.tabs.TAB_ID_NONE],
                    },
                },
            ],
        },
        () => {
            console.log('Declarative network request rules set.')
        },
    )
} else {
    browserApi.getWebRequestApi().onBeforeSendHeaders.addListener(
        function (details) {
            const requestHeaders = details.requestHeaders

            // tabId == -1 means that TD is loading in the add-in. Higher IDs mean that TD is loading in a tab, i.e., not within the extension.
            if (details.tabId !== -1) {
                return {
                    requestHeaders,
                }
            }

            const resultingHeaders = addDoistPlatformHeader(addDoistVersionHeader(requestHeaders))

            return {
                requestHeaders: resultingHeaders,
            }
        },
        {
            urls: [`*://${DOMAIN}/*`],
        },
        ['requestHeaders', 'blocking'],
    )
}
