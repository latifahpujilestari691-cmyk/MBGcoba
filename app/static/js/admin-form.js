/**
 * Admin Form Utilities — image preview & galeri field toggle
 * Used by: blog_form, galeri_form, produk_form
 */

/** Show a preview of the selected image file */
function previewImage(input) {
  const preview = document.getElementById('preview');
  if (input.files && input.files[0]) {
    preview.src = URL.createObjectURL(input.files[0]);
    preview.style.display = 'block';
  }
}

/** Toggle between photo & testimonial fields in galeri_form */
function toggleFields() {
  const isTestimoni = document.getElementById('typeSelect').value === 'testimonial';
  document.getElementById('fieldsPhoto').style.display     = isTestimoni ? 'none' : 'block';
  document.getElementById('fieldsTestimoni').style.display = isTestimoni ? 'block' : 'none';
}

// Auto-run toggleFields on pages that have #typeSelect (galeri_form)
document.addEventListener('DOMContentLoaded', function () {
  if (document.getElementById('typeSelect')) {
    toggleFields();
  }
});
