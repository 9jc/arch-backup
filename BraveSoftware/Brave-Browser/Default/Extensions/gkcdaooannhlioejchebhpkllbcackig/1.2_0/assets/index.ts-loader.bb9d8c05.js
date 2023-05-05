(function () {
  'use strict';

  (async () => {
    await import(
      /* @vite-ignore */
      chrome.runtime.getURL("assets/index.ts.c78b64b6.js")
    );
  })().catch(console.error);

})();
