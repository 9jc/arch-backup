const browserApi = {
    withActiveTab: function (action) {
        chrome.tabs.getSelected(null, function (tab) {
            if (tab) {
                action(tab)
            }
        })
    },

    tabsQuery: function (query, action) {
        chrome.tabs.query(query, action)
    },

    tabsUpdate: function (id, data) {
        chrome.tabs.update(id, data)
    },

    sendRequest: function (message) {
        chrome.extension.sendRequest(message, function () {})
    },

    addRequestListener: function (listener) {
        chrome.extension.onRequest.addListener(listener)
    },

    addCommandListener: function (listener) {
        chrome.commands.onCommand.addListener(listener)
    },

    getExtensionOptions: function (callback) {
        function readOptionFromStorage() {
            chrome.storage.sync.get(['withDueToday'], function (items) {
                callback({
                    withDueToday: items.withDueToday,
                })
            })
        }

        readOptionFromStorage()
    },

    addExtensionOptionsChangedListener: function (callback) {
        chrome.storage.onChanged.addListener(callback)
    },

    setExtensionOptions: function (options, callback) {
        chrome.storage.sync.set(options, callback)
    },

    windowCreate: function (window, allowScriptsToClose) {
        if (allowScriptsToClose) {
            window.setSelfAsOpener = true
        }

        chrome.windows.create(window)
    },

    windowGetCurrent: function (callback) {
        chrome.windows.getCurrent(callback)
    },

    contextMenuCreate: function (menu, listener) {
        chrome.contextMenus.create(menu)
        chrome.contextMenus.onClicked.addListener(listener)
    },

    getLocalizedMessage: function (code) {
        return chrome.i18n.getMessage(code)
    },

    getBackgroundPage: function () {
        return chrome.extension.getBackgroundPage()
    },

    canAccessBackgroundPage: function () {
        return true
    },

    getWebRequestApi: function () {
        return chrome.webRequest
    },

    getRuntimeApi: function () {
        return chrome.runtime
    },
}
