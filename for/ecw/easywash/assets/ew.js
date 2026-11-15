// EasyWash for business, variations A and B: plate demo, lane, tabs, calculator, call form.
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var eur = function (n) { return '€' + Math.round(n).toLocaleString('en-GB'); };
  var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // the visitor's plate, carried through the page (and across A, B and C)
  var input = $('#plate');
  function clean(v) { return (v || '').toUpperCase().replace(/[^A-Z0-9 -]/g, '').slice(0, 8); }
  function setPlate(v) {
    var p = clean(v) || 'ABC-123';
    $$('[data-plate]').forEach(function (el) { el.textContent = p; });
    try { sessionStorage.setItem('ewPlate', p); } catch (e) {}
    return p;
  }
  var saved = null;
  try { saved = sessionStorage.getItem('ewPlate'); } catch (e) {}
  if (saved) { setPlate(saved); if (input) input.value = clean(saved); }
  if (input) input.addEventListener('input', function () { input.value = clean(input.value); setPlate(input.value); });

  // bay demo: the five lines light up in order
  var bay = $('#bay'), timers = [];
  function drive() {
    var lines = $$('.log li', bay);
    timers.forEach(clearTimeout); timers = [];
    lines.forEach(function (l) { l.classList.remove('on'); });
    lines.forEach(function (l, i) {
      timers.push(setTimeout(function () { l.classList.add('on'); }, still ? 0 : 350 + i * 650));
    });
  }
  if (bay) {
    bay.addEventListener('submit', function (e) { e.preventDefault(); setPlate(input.value); drive(); });
    setTimeout(drive, 500);
  }

  // lane: the plate drives the four stops once, when the view arrives
  var lane = $('#lane');
  if (lane && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (en) {
      if (en[0].isIntersecting) { lane.classList.add('go'); io.disconnect(); }
    }, { threshold: 0.5 });
    io.observe(lane);
  } else if (lane) { lane.classList.add('go'); }

  // tabs (platform parts and customers)
  $$('[data-tabs]').forEach(function (list) {
    var tabs = $$('[role="tab"]', list);
    function select(t, focus) {
      tabs.forEach(function (x) {
        var on = x === t;
        x.setAttribute('aria-selected', String(on));
        x.tabIndex = on ? 0 : -1;
        var p = document.getElementById(x.getAttribute('aria-controls'));
        if (p) p.hidden = !on;
      });
      if (focus) t.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t); });
      t.addEventListener('keydown', function (e) {
        var d = (e.key === 'ArrowDown' || e.key === 'ArrowRight') ? 1 : (e.key === 'ArrowUp' || e.key === 'ArrowLeft') ? -1 : 0;
        if (!d) return;
        e.preventDefault();
        select(tabs[(i + d + tabs.length) % tabs.length], true);
      });
    });
  });

  // calculator
  var sites = $('#c-sites'), mem = $('#c-mem'), price = $('#c-price');
  function fill(el) { el.style.setProperty('--p', ((el.value - el.min) / (el.max - el.min) * 100) + '%'); }
  function calc() {
    if (!sites) return;
    var m = sites.value * mem.value * price.value;
    $('#o-sites').textContent = sites.value;
    $('#o-mem').textContent = mem.value;
    $('#o-price').textContent = '€' + price.value;
    $('#o-month').textContent = eur(m);
    $('#o-year').textContent = eur(m * 12);
    [sites, mem, price].forEach(fill);
  }
  [sites, mem, price].forEach(function (el) { if (el) el.addEventListener('input', calc); });
  calc();

  // call form: one question, then details, then the calendar
  var step = 1;
  function showStep(n) {
    step = n;
    $$('.fstep').forEach(function (f) { f.hidden = Number(f.dataset.step) !== n; });
    $$('.form .prog i').forEach(function (i, idx) { i.classList.toggle('on', idx < n); });
  }
  $$('[data-sites] .chip').forEach(function (c) {
    c.addEventListener('click', function () {
      $$('[data-sites] .chip').forEach(function (x) { x.setAttribute('aria-pressed', String(x === c)); });
      if (c.dataset.v !== 'dealer' && sites) { sites.value = c.dataset.v; calc(); }
      showStep(2);
      var f = $('#f-name'); if (f) f.focus({ preventScroll: true });
    });
  });
  $$('[data-next]').forEach(function (b) { b.addEventListener('click', function () { showStep(3); }); });
  $$('[data-back]').forEach(function (b) { b.addEventListener('click', function () { showStep(step - 1); }); });
  var form = $('#form');
  if (form) form.addEventListener('submit', function (e) { e.preventDefault(); });
})();
