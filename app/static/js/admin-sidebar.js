/**
 * Admin Sidebar — toggle & auto-close on mobile
 * Used by: dashboard, blog_list, faq_list, galeri_list, produk_list
 */
function toggleMobileSidebar() {
  const sidebar = document.querySelector('.admin-sidebar');
  const overlay = document.querySelector('.sidebar-overlay');

  sidebar.classList.toggle('active');
  overlay.classList.toggle('active');
}

// Close sidebar when clicking any nav link (mobile behaviour)
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.admin-sidebar .nav-link').forEach(function (link) {
    link.addEventListener('click', function () {
      const sidebar = document.querySelector('.admin-sidebar');
      const overlay = document.querySelector('.sidebar-overlay');

      sidebar.classList.remove('active');
      overlay.classList.remove('active');
    });
  });
});