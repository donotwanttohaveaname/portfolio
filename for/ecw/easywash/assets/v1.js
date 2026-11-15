// EasyWash for business concept: site chips, platform tabs, calculator, form steps, mobile CTA.
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var eur = function (n) { return '€' + Math.round(n).toLocaleString('en-GB'); };

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

  // site-count chips (hero and form share the answer)
  var step = 1;
  function showStep(n) {
    step = n;
    $$('.fstep').forEach(function (f) { f.hidden = Number(f.dataset.step) !== n; });
    $$('.form .prog i').forEach(function (i, idx) { i.classList.toggle('on', idx < n); });
  }
  function pick(v) {
    $$('[data-sites] .chip').forEach(function (c) { c.setAttribute('aria-pressed', String(c.dataset.v === v)); });
    if (v !== 'dealer' && sites) { sites.value = v; calc(); }
  }
  $$('[data-sites] .chip').forEach(function (c) {
    c.addEventListener('click', function () {
      var v = c.dataset.v, inForm = !!c.closest('.form');
      pick(v);
      if (inForm) { showStep(2); var f = $('#f-name'); if (f) f.focus({ preventScroll: true }); return; }
      var target = $(v === 'dealer' ? '#who' : '#numbers');
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      if (step === 1) showStep(2);
    });
  });
  $$('[data-next]').forEach(function (b) { b.addEventListener('click', function () { showStep(3); }); });
  $$('[data-back]').forEach(function (b) { b.addEventListener('click', function () { showStep(step - 1); }); });
  var form = $('#form');
  if (form) form.addEventListener('submit', function (e) { e.preventDefault(); });

  // platform tabs
  var tabs = $$('.tab');
  function select(t, focus) {
    tabs.forEach(function (x) {
      var on = x === t;
      x.setAttribute('aria-selected', String(on));
      x.tabIndex = on ? 0 : -1;
      var p = document.getElementById(x.getAttribute('aria-controls'));
      if (p) p.hidden = !on;
    });
    if (focus) t.focus();
    if (t.scrollIntoView && window.matchMedia('(max-width:1000px)').matches) {
      t.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    }
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

  // sticky mobile CTA: after the hero, hidden while the form is on screen
  var mcta = $('#mcta'), hero = $('.hero'), call = $('#call');
  if (mcta && hero && call && 'IntersectionObserver' in window) {
    var pastHero = false, atForm = false;
    var upd = function () { mcta.classList.toggle('show', pastHero && !atForm); };
    new IntersectionObserver(function (e) { pastHero = !e[0].isIntersecting; upd(); }).observe(hero);
    new IntersectionObserver(function (e) { atForm = e[0].isIntersecting; upd(); }, { threshold: 0.15 }).observe(call);
  }
})();
