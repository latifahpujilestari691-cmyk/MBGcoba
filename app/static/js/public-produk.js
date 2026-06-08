/**
 * Public Produk — filter reset button active state
 * Used by: produk.html
 */
document.addEventListener('DOMContentLoaded', function() {
  var categorySelect = document.querySelector('select[name="category"]');
  var resetBtn = document.querySelector('.btn-reset');
  var searchInput = document.querySelector('input[name="q"]');

  if (!categorySelect || !resetBtn || !searchInput) return;

  function toggleResetBtn() {
    if (categorySelect.value !== '' || searchInput.value.trim() !== '') {
      resetBtn.classList.add('btn-reset-active');
    } else {
      resetBtn.classList.remove('btn-reset-active');
    }
  }

  categorySelect.addEventListener('change', toggleResetBtn);
  searchInput.addEventListener('input', toggleResetBtn);
});