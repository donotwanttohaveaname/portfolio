// One screen per view (original A and B). Measures the bars around the views, then scales a view's
// content down just enough when the screen is too short for it. Laptop and desktop widths only.
(function () {
  var wide = window.matchMedia('(min-width: 941px)');
  var root = document.documentElement;
  function h(sel) { var e = document.querySelector(sel); return e ? e.offsetHeight : 0; }
  function fit() {
    var views = Array.prototype.slice.call(document.querySelectorAll('.hero, .proof, section.sec'));
    views.forEach(function (v) { var w = v.querySelector(':scope > .wrap'); if (w) w.style.zoom = ''; });
    if (!wide.matches) return;
    root.style.setProperty('--top', (h('.concept') + h('.nav')) + 'px');
    root.style.setProperty('--strip', h('.strip') + 'px');
    root.style.setProperty('--foot', h('footer') + 'px');
    views.forEach(function (v) {
      var w = v.querySelector(':scope > .wrap');
      if (!w) return;
      var cs = getComputedStyle(v);
      var room = parseFloat(cs.minHeight) - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
      var need = w.offsetHeight;
      if (need > room + 0.5) w.style.zoom = Math.max(0.55, room / need).toFixed(4);
    });
  }
  var t;
  function later() { clearTimeout(t); t = setTimeout(fit, 80); }
  fit();
  window.addEventListener('resize', later);
  window.addEventListener('load', fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
  // opening an FAQ answer or switching a platform tab changes a view's height
  document.addEventListener('toggle', later, true);
  document.addEventListener('click', function (e) { if (e.target.closest('.tab, .chip, [data-next], [data-back]')) later(); });
})();
