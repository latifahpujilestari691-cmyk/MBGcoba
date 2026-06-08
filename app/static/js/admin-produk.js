/**
 * Admin Produk — Kategori Modal CRUD (AJAX)
 * Used by: produk_list.html
 */
let currentKategoriId = null;

function openKategoriModal() {
  document.getElementById('modalKategori').style.display = 'flex';
  loadKategoriList();
}

function closeKategoriModal() {
  document.getElementById('modalKategori').style.display = 'none';
  document.getElementById('formMessage').style.display = 'none';
  document.getElementById('formMessage').innerHTML = '';
}

function showMessage(message, type) {
  const msgDiv = document.getElementById('formMessage');
  msgDiv.textContent = message;
  msgDiv.style.display = 'block';
  msgDiv.style.backgroundColor = type === 'success' ? '#d4edda' : '#f8d7da';
  msgDiv.style.color = type === 'success' ? '#155724' : '#721c24';
  msgDiv.style.borderColor = type === 'success' ? '#c3e6cb' : '#f5c6cb';
  msgDiv.style.border = '1px solid';
}

function hideMessage() {
  const msgDiv = document.getElementById('formMessage');
  msgDiv.style.display = 'none';
}

function openKategoriForm(action) {
  currentKategoriId = action === 'new' ? null : action;
  document.getElementById('modalTitle').textContent = currentKategoriId ? 'Edit Kategori' : 'Tambah Kategori';
  document.getElementById('kategoriListView').style.display = 'none';
  document.getElementById('kategoriFormView').style.display = 'block';
  hideMessage();

  fetch('/admin/api/kategori/form/' + action)
    .then(function (res) { return res.json(); })
    .then(function (data) {
      document.getElementById('formContent').innerHTML = data.html;
      document.getElementById('kategori_name').focus();
    })
    .catch(function (err) { showMessage('Error loading form: ' + err, 'error'); });
}

function closeKategoriForm() {
  document.getElementById('modalTitle').textContent = 'Kelola Kategori';
  document.getElementById('kategoriFormView').style.display = 'none';
  document.getElementById('kategoriListView').style.display = 'block';
  hideMessage();
  loadKategoriList();
}

function saveKategori(kategoriId) {
  var name = document.getElementById('kategori_name').value.trim();
  if (!name) {
    showMessage('Nama kategori tidak boleh kosong', 'error');
    return;
  }

  var payload = {
    name: name,
    id: kategoriId || null
  };

  fetch('/admin/api/kategori/simpan', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
    .then(function (res) { return res.json(); })
    .then(function (data) {
      if (data.success) {
        showMessage(data.message, 'success');
        setTimeout(function () { closeKategoriForm(); }, 1500);
      } else {
        showMessage(data.error || 'Terjadi kesalahan', 'error');
      }
    })
    .catch(function (err) { showMessage('Error: ' + err, 'error'); });
}

function loadKategoriList() {
  fetch('/admin/api/kategori/list')
    .then(function (res) { return res.json(); })
    .then(function (data) {
      var tbody = document.getElementById('kategoriTableBody');
      if (data.categories.length === 0) {
        tbody.innerHTML = '<tr><td colspan="2" class="text-center text-muted py-4">Belum ada kategori.</td></tr>';
        return;
      }

      var html = '';
      data.categories.forEach(function (cat) {
        html += '<tr>' +
          '<td><strong>' + cat.name + '</strong></td>' +
          '<td>' +
            '<div class="d-flex gap-1">' +
              '<button type="button" onclick="openKategoriForm(' + cat.id + ')" class="btn-edit">Edit</button>' +
              '<button type="button" onclick="deleteKategori(' + cat.id + ')" class="btn-delete">Hapus</button>' +
            '</div>' +
          '</td>' +
        '</tr>';
      });
      tbody.innerHTML = html;
    })
    .catch(function (err) { console.error('Error loading kategori:', err); });
}

function deleteKategori(kategoriId) {
  if (!confirm('Hapus kategori ini? Kategori yang masih digunakan tidak bisa dihapus.')) {
    return;
  }

  fetch('/admin/api/kategori/hapus/' + kategoriId, { method: 'DELETE' })
    .then(function (res) { return res.json(); })
    .then(function (data) {
      if (data.success) {
        showMessage(data.message, 'success');
        setTimeout(function () { loadKategoriList(); }, 1000);
      } else {
        showMessage(data.error || 'Terjadi kesalahan', 'error');
      }
    })
    .catch(function (err) { showMessage('Error: ' + err, 'error'); });
}

// Close modal when clicking outside of it
document.addEventListener('DOMContentLoaded', function () {
  var modal = document.getElementById('modalKategori');
  if (modal) {
    modal.addEventListener('click', function (e) {
      if (e.target === this) {
        closeKategoriModal();
      }
    });
  }
});