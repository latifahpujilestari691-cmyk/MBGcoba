/**
 * Base Public — announcement bar & scroll reveal animations
 * Used by: base.html (extends ke semua halaman public)
 */

// Announcement bar — build marquee items
(function () {
  var items = [
    { icon: '💸', text: 'Payment: Transfer / Cash' },
    { icon: '🛒', text: 'Minimal Order 25 Pcs untuk Produk Tertentu' },
    { icon: '🚚', text: 'Melayani Delivery Pesanan' },
    { icon: '🎂', text: 'Open for Request' }
  ];
  var track = document.getElementById('announcementTrack');
  if (!track) return;
  function buildItem(item) {
    return '<span class="announcement-item"><span class="ann-icon">' + item.icon + '</span>' + item.text + '</span><span class="announcement-sep">✦</span>';
  }
  var html = '';
  for (var r = 0; r < 2; r++) {
    items.forEach(function (item) { html += buildItem(item); });
  }
  track.innerHTML = html;
})();

// Scroll reveal — IntersectionObserver
(function () {
  var SELECTORS = 'section, .product-card, .blog-card, .profil-box, .gallery-item, .hero, .page-header, .kontak-box, .site-footer';

  document.addEventListener('DOMContentLoaded', function () {
    var els = Array.from(document.querySelectorAll(SELECTORS));

    els.forEach(function (el) { el.classList.add('reveal-on-scroll'); });

    if ('IntersectionObserver' in window) {
      var obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            obs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.08 });

      els.forEach(function (el) { obs.observe(el); });
    } else {
      els.forEach(function (el) { el.classList.add('is-visible'); });
    }
  });
})();