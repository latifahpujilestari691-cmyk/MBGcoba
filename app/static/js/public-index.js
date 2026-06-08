/**
 * Public Index — testimonial lightbox
 * Used by: index.html
 */
function openTesLightbox(src) {
  document.getElementById('tesLightbox-img').src = src;
  document.getElementById('tesLightbox').classList.add('active');
}
function closeTesLightbox() {
  document.getElementById('tesLightbox').classList.remove('active');
}
document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeTesLightbox(); });