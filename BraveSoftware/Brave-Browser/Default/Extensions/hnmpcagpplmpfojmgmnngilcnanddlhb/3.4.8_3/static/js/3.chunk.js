(window.webpackJsonp=window.webpackJsonp||[]).push([[3],{814:function(t,n,e){"use strict";e.r(n);var r=e(12),a=e(4),o=e.n(a),i=e(21),c=e(6),s=e(20),u=e(125),w=e(88),d=e(65),p=e(16),b=e.n(p),f=e(61),l=e(5),v=e(55),h=function(){return browser.cookies.getAll({}).then(function(t){for(var n,e,r=t.length,a=0;a<r;a++)e="http"+((n=t[a]).secure?"s":"")+"://"+n.domain+n.path,browser.cookies.remove({url:e,name:n.name})})},S=e(2);n.default=Object(c.a)(o.a.mark(function t(){var n;return o.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,Object(w.a)();case 2:return window.ipAddress=t.sent,window.checkIp=w.a,window.constants=l,window.sleep=u.a,window.db=Object(v.a)(),window.constructDebugLog=d.a,window.CLIENT_AUTH_SECRET=l.CLIENT_AUTH_SECRET,window.store=S.b,window.actions=S.a,window.globals=f.a,t.next=14,f.a.ENV;case 14:window.ENV=t.sent,window.TEST_LOCATION=l.ENVS[window.ENV].TEST_LOCATION,window.api=s.a,window.removeAllCookies=h,window.windscribeListUrl="https://assets.windscribe.com/extension/ws",n=function(t){var n=0;return Object(c.a)(o.a.mark(function e(){var r,a,c,s=arguments;return o.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:for(r=s.length,a=new Array(r),c=0;c<r;c++)a[c]=s[c];return e.next=3,t.apply(void 0,Object(i.a)(a.concat(n,20)));case 3:n=0;case 4:case"end":return e.stop()}},e)}))},window.setView=function(t){return S.b.dispatch(S.a.view.set(t))},window.turnOffProxy=Object(c.a)(o.a.mark(function t(){return o.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.abrupt("return",new Promise(function(t){var n=S.b.subscribe(function(){"disconnected"===S.b.getState().proxy.status&&(n(),t())});S.b.dispatch(S.a.proxy.deactivate())}));case 1:case"end":return t.stop()}},t)})),window.login=function(){var t=Object(c.a)(o.a.mark(function t(n){return o.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.abrupt("return",new Promise(function(t){var e=S.b.subscribe(function(){S.b.getState().cruiseControlList.data&&(e(),t())});S.b.dispatch(S.a.auth.login(n))}));case 1:case"end":return t.stop()}},t)}));return function(n){return t.apply(this,arguments)}}(),window.logout=function(){var t=Object(c.a)(o.a.mark(function t(n){return o.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.abrupt("return",new Promise(function(t){var e=S.b.subscribe(function(){var n,r;(null===(n=S.b.getState())||void 0===n?void 0:null===(r=n.session)||void 0===r?void 0:r.username)||(e(),t())});S.b.dispatch(S.a.auth.logout(n))}));case 1:case"end":return t.stop()}},t)}));return function(n){return t.apply(this,arguments)}}(),window.setLocation=n(function(){var t=Object(c.a)(o.a.mark(function t(n,e,r){return o.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.abrupt("return",new Promise(function(t){var a=S.b.subscribe(function(){++e>r&&(a(),t()),S.b.getState().currentLocation.name===n.name&&"connected"===S.b.getState().proxy.status&&(a(),t()),S.b.getState().currentLocation.name===n.name&&"disconnected"===S.b.getState().proxy.status&&S.b.dispatch(S.a.proxy.activate())});S.b.dispatch(S.a.currentLocation.set(n))}));case 1:case"end":return t.stop()}},t)}));return function(n,e,r){return t.apply(this,arguments)}}()),window.setENV=function(){var t=Object(c.a)(o.a.mark(function t(n){return o.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return window.ENV=n,t.next=3,browser.storage.local.set({ENV:n,API_URL:l.ENVS[n].API_URL,ASSETS_URL:l.ENVS[n].ASSETS_URL});case 3:s.a.setConfig({apiUrl:l.ENVS[n].API_URL,assetsUrl:l.ENVS[n].ASSETS_URL});case 4:case"end":return t.stop()}},t)}));return function(n){return t.apply(this,arguments)}}(),window.helpers={createWhitelistShape:function(t){var n=t.domain,e=t.config,a=void 0===e?{}:e,o={domain:n,includeAllSubdomains:!0,allowDirectConnect:!1,allowAds:!1,allowCookies:!1};return Object(r.a)({},o,a)},waitForStoreValue:function(t){var n=t.action,e=t.pathToStateValue;return new Promise(function(t){var r=S.b.subscribe(function(){var n=b.a.get(S.b.getState(),e);n&&(r(),t(n))});S.b.dispatch(n)})},removeLists:function(t){return t.reduce(function(t,n){return t.then(function(){S.b.dispatch(S.a.blockListsEnabled.toggle(n)),Promise.resolve()})},Promise.resolve())}};case 27:case"end":return t.stop()}},t)}))}}]);