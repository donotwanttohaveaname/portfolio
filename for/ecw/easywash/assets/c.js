// EasyWash for business, version C: follow one car.
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var eur = function (n) { return '€' + Math.round(n).toLocaleString('en-GB'); };
  document.documentElement.classList.add('js');

  // the plate is the main character: typed once, shown everywhere (shared with A and B)
  var input = $('#plate');
  function clean(v) { return (v || '').toUpperCase().replace(/[^A-Z0-9 -]/g, '').slice(0, 8); }
  function setPlate(v) {
    var p = clean(v) || 'ABC-123';
    $$('[data-plate]').forEach(function (el) { el.textContent = p; });
    try { sessionStorage.setItem('ewPlate', p); } catch (e) {}
  }
  var saved = null;
  try { saved = sessionStorage.getItem('ewPlate'); } catch (e) {}
  if (saved) { setPlate(saved); input.value = clean(saved); }
  input.addEventListener('input', function () { input.value = clean(input.value); setPlate(input.value); });
  $('#start').addEventListener('submit', function (e) {
    e.preventDefault();
    setPlate(input.value);
    $('#first').scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  // one month: renewal on day 1, five washes, a week of rain
  var month = $('#month'), wash = [3, 9, 12, 21, 27], rain = [13, 14, 15, 16, 17, 18, 19];
  for (var d = 1; d <= 30; d++) {
    var c = document.createElement('i');
    c.style.setProperty('--i', d);
    if (d === 1) c.className = 'pay'; else if (wash.indexOf(d) > -1) c.className = 'w'; else if (rain.indexOf(d) > -1) c.className = 'r';
    month.appendChild(c);
  }

  // each view plays once when it arrives; the HUD follows the car
  var t = $('#hud-t'), s = $('#hud-s'), views = $$('.v');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('in');
        t.textContent = en.target.dataset.t || '';
        s.textContent = en.target.dataset.s || '';
      });
    }, { threshold: 0.55 });
    views.forEach(function (v) { io.observe(v); });
  } else {
    views.forEach(function (v) { v.classList.add('in'); });
  }

  // the rating is a real control
  var out = $('#rate-out');
  $$('.scale button').forEach(function (b) {
    b.addEventListener('click', function () {
      $$('.scale button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      var n = Number(b.textContent);
      out.textContent = n >= 4
        ? 'Saved. It counts towards the site\'s score, next to turnover in the dashboard.'
        : 'Saved. The site manager gets an alert now, while the driver is still on the forecourt.';
    });
  });

  // count the cars
  var sites = $('#c-sites'), mem = $('#c-mem'), PRICE = 29.9;
  function fill(el) { el.style.setProperty('--p', ((el.value - el.min) / (el.max - el.min) * 100) + '%'); }
  function calc() {
    var m = sites.value * mem.value * PRICE;
    $('#o-sites').textContent = sites.value;
    $('#o-mem').textContent = mem.value;
    $('#o-month').textContent = eur(m);
    $('#o-year').textContent = eur(m * 12);
    [sites, mem].forEach(fill);
  }
  [sites, mem].forEach(function (el) { el.addEventListener('input', calc); });
  calc();

  // call form
  var step = 1;
  function showStep(n) {
    step = n;
    $$('.fstep').forEach(function (f) { f.hidden = Number(f.dataset.step) !== n; });
    $$('.form .prog i').forEach(function (i, idx) { i.classList.toggle('on', idx < n); });
  }
  $$('[data-sites] .chip').forEach(function (c) {
    c.addEventListener('click', function () {
      $$('[data-sites] .chip').forEach(function (x) { x.setAttribute('aria-pressed', String(x === c)); });
      if (c.dataset.v !== 'dealer') { sites.value = c.dataset.v; calc(); }
      showStep(2);
      $('#f-name').focus({ preventScroll: true });
    });
  });
  $$('[data-next]').forEach(function (b) { b.addEventListener('click', function () { showStep(3); }); });
  $$('[data-back]').forEach(function (b) { b.addEventListener('click', function () { showStep(step - 1); }); });
  $('#form').addEventListener('submit', function (e) { e.preventDefault(); });
})();
