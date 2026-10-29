/* Open links to R2 in a separate browser tab.
 *
 * Links to the R2 web application (hosts below) open in one shared tab
 * named "r2": the first click opens a new tab, later clicks reuse it.
 * Set OTHER_EXTERNAL_NEW_TAB to true to also open all other external
 * links (other websites) in a new tab.
 * Loaded on every page via app.add_js_file() in conf.py.
 */
(function () {
  var R2_HOSTS = ['hgserver1.amc.nl', 'hgserver2.amc.nl', 'r2.amc.nl'];
  var R2_TARGET = 'r2';
  var OTHER_EXTERNAL_NEW_TAB = true;

  function setTargets() {
    var links = document.querySelectorAll('a[href]');
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      if (a.hostname === window.location.hostname) { continue; }
      if (R2_HOSTS.indexOf(a.hostname) !== -1) {
        a.target = R2_TARGET;
      } else if (OTHER_EXTERNAL_NEW_TAB && /^https?:$/.test(a.protocol)) {
        a.target = '_blank';
        a.rel = 'noopener';
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setTargets);
  } else {
    setTargets();
  }
})();
