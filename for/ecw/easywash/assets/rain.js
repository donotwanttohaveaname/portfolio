// Version C: the rain or shine switch. One site, one week, illustrative figures:
// 200 members at EUR 29.90 a month (EUR 1,380 a week) and single washes at EUR 12.
(function () {
  var sec = document.getElementById('weather');
  if (!sec) return;
  var week = sec.querySelector('.week'), btns = Array.prototype.slice.call(sec.querySelectorAll('[data-wx]'));
  var MEMBER = 1380, SINGLE = { dry: 1800, wet: 360 };
  var eur = function (n) { return '€' + n.toLocaleString('en-GB'); };
  function set(state) {
    var total = SINGLE[state] + MEMBER, share = Math.round(MEMBER / total * 100);
    week.dataset.state = state;
    sec.classList.toggle('wet', state === 'wet');
    btns.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.wx === state)); });
    document.getElementById('wx-single').textContent = eur(SINGLE[state]);
    document.getElementById('wx-total').textContent = eur(total);
    document.getElementById('wx-say').textContent = state === 'wet'
      ? 'Rainy week. Single washes fell by ' + eur(SINGLE.dry - SINGLE.wet) + '. Memberships did not move, and now bring in ' + share + '% of the income.'
      : 'Dry week. Memberships bring in ' + share + '% of the income.';
  }
  btns.forEach(function (b) { b.addEventListener('click', function () { set(b.dataset.wx); }); });
  set('dry');
})();
