/* Snoozetown — plate viewer and night-observation mode.
   No dependencies. Degrades to a plain scrolling document without JS. */

(function () {
  'use strict';

  /* ---------- night observation mode ---------- */

  var html = document.documentElement;
  var toggle = document.getElementById('mode');
  var STORE = 'snoozetown-mode';

  function apply(mode) {
    html.setAttribute('data-mode', mode);
    toggle.setAttribute('aria-pressed', String(mode === 'night'));
  }

  var saved = null;
  try { saved = localStorage.getItem(STORE); } catch (e) { /* private mode */ }
  if (saved) {
    apply(saved);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    apply('night');
  } else {
    apply('day');
  }

  toggle.addEventListener('click', function () {
    var next = html.getAttribute('data-mode') === 'night' ? 'day' : 'night';
    apply(next);
    try { localStorage.setItem(STORE, next); } catch (e) { /* ignore */ }
  });

  /* ---------- plate viewer ---------- */

  var plates = Array.prototype.slice.call(document.querySelectorAll('.plate'));
  var box = document.getElementById('lightbox');
  var img = document.getElementById('lb-img');
  var cap = document.getElementById('lb-cap');
  var current = 0;
  var lastFocused = null;

  function show(i) {
    current = (i + plates.length) % plates.length;
    var plate = plates[current];
    var thumb = plate.querySelector('img');
    var specimen = plate.closest('.specimen');
    var desig = specimen.querySelector('.desig').firstChild.textContent.trim();
    var dd = specimen.querySelectorAll('.fields dd');   // [0] date, [1] time
    var stamp = dd[0].textContent.trim() + ', ' + dd[1].textContent.trim();

    img.src = plate.dataset.full;
    img.alt = thumb.alt;
    cap.textContent = desig + ' — ' + stamp + ' · ' + (current + 1) + ' of ' + plates.length;
  }

  function open(i) {
    lastFocused = document.activeElement;
    show(i);
    box.hidden = false;
    document.body.style.overflow = 'hidden';
    box.querySelector('.lb-close').focus();
  }

  function close() {
    box.hidden = true;
    img.src = '';
    document.body.style.overflow = '';
    if (lastFocused) lastFocused.focus();
  }

  plates.forEach(function (plate, i) {
    plate.addEventListener('click', function () { open(i); });
  });

  box.querySelector('.lb-close').addEventListener('click', close);
  box.querySelector('.lb-prev').addEventListener('click', function () { show(current - 1); });
  box.querySelector('.lb-next').addEventListener('click', function () { show(current + 1); });

  box.addEventListener('click', function (e) {
    if (e.target === box || e.target.tagName === 'FIGURE') close();
  });

  document.addEventListener('keydown', function (e) {
    if (box.hidden) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(current - 1);
    else if (e.key === 'ArrowRight') show(current + 1);
    else if (e.key === 'Tab') {
      // keep focus inside the dialog
      var focusable = box.querySelectorAll('button');
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  /* swipe on touch devices */
  var x0 = null;
  box.addEventListener('touchstart', function (e) { x0 = e.changedTouches[0].clientX; }, { passive: true });
  box.addEventListener('touchend', function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) show(current + (dx < 0 ? 1 : -1));
    x0 = null;
  }, { passive: true });
})();
