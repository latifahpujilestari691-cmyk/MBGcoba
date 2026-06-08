import os
import re
import bcrypt
from flask import Blueprint, render_template, session, request, redirect, url_for, flash, jsonify
from app.models.helpers import login_required
from app.models.db import get_connection
from werkzeug.utils import secure_filename

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text

admin_bp = Blueprint('admin', __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'static', 'images')
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ── DASHBOARD ──────────────────────────────────────────────
@admin_bp.route('/dashboard')
@login_required
def dashboard():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) AS total FROM products WHERE is_active = 1")
            total_produk = cur.fetchone()['total']
            cur.execute("SELECT COUNT(*) AS total FROM articles WHERE is_published = 1")
            total_artikel = cur.fetchone()['total']
            cur.execute("SELECT COUNT(*) AS total FROM gallery WHERE type = 'photo'")
            total_foto = cur.fetchone()['total']
            cur.execute("SELECT COUNT(*) AS total FROM gallery WHERE type = 'testimonial'")
            total_testi = cur.fetchone()['total']
    finally:
        conn.close()
    return render_template('admin/dashboard.html',
                           total_produk=total_produk,
                           total_artikel=total_artikel,
                           total_foto=total_foto,
                           total_testi=total_testi)


# ── KATEGORI AJAX (untuk modal) ────────────────────────────
@admin_bp.route('/api/kategori/form/<action>', methods=['GET', 'POST'])
@login_required
def kategori_form_ajax(action):
    """Load form kategori untuk modal (tambah atau edit)"""
    kategori = None
    if action.isdigit():
        # Edit mode
        kategori_id = int(action)
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name FROM categories WHERE id = %s", (kategori_id,))
                kategori = cur.fetchone()
        finally:
            conn.close()
        if not kategori:
            return jsonify({'error': 'Kategori tidak ditemukan'}), 404
    
    # Return form HTML
    kategori_name = kategori['name'] if kategori else ''
    kategori_id = kategori['id'] if kategori else None
    form_html = '''
    <div style="margin-bottom: 1.5rem;">
        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #333;">Nama Kategori</label>
        <input type="text" id="kategori_name" class="form-control" placeholder="Masukkan nama kategori" value="''' + kategori_name + '''" required />
    </div>
    <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
        <button type="button" onclick="saveKategori(''' + str(kategori_id) + ''')" class="btn-save">💾 Simpan</button>
        <button type="button" onclick="closeKategoriForm()" class="btn-cancel">Batal</button>
    </div>
    '''
    return jsonify({'html': form_html, 'is_edit': bool(kategori), 'kategori_id': kategori_id})


@admin_bp.route('/api/kategori/simpan', methods=['POST'])
@login_required
def kategori_simpan_ajax():
    """Simpan kategori (tambah atau edit) via AJAX"""
    data = request.get_json()
    name = data.get('name', '').strip()
    kategori_id = data.get('id')
    
    if not name:
        return jsonify({'error': 'Nama kategori tidak boleh kosong'}), 400
    
    conn = get_connection()
    try:
        slug = slugify(name)
        with conn.cursor() as cur:
            if kategori_id:
                # Update
                cur.execute("UPDATE categories SET name=%s, slug=%s WHERE id=%s", (name, slug, kategori_id))
                msg = 'Kategori berhasil diupdate!'
            else:
                # Insert
                cur.execute("INSERT INTO categories (name, slug) VALUES (%s, %s)", (name, slug))
                msg = 'Kategori berhasil ditambahkan!'
        conn.commit()
        return jsonify({'success': True, 'message': msg})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()


@admin_bp.route('/api/kategori/list', methods=['GET'])
@login_required
def kategori_list_ajax():
    """Get daftar kategori via AJAX (JSON)"""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM categories ORDER BY name")
            categories = cur.fetchall()
    finally:
        conn.close()
    
    # Convert to list of dicts
    cat_list = [{'id': c['id'], 'name': c['name']} for c in categories]
    return jsonify({'categories': cat_list})


@admin_bp.route('/api/kategori/hapus/<int:id>', methods=['DELETE'])
@login_required
def kategori_hapus_ajax(id):
    """Hapus kategori via AJAX"""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM categories WHERE id = %s", (id,))
        conn.commit()
        return jsonify({'success': True, 'message': 'Kategori berhasil dihapus.'})
    except Exception as e:
        return jsonify({'error': 'Tidak bisa hapus kategori yang masih digunakan produk.'}), 400
    finally:
        conn.close()



# ── KATEGORI LIST ─────────────────────────────────────────
@admin_bp.route('/kategori')
@login_required
def kategori_list():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, slug, description FROM categories ORDER BY name")
            categories = cur.fetchall()
    finally:
        conn.close()
    return render_template('admin/kategori_list.html', categories=categories)


@admin_bp.route('/kategori/tambah', methods=['GET', 'POST'])
@login_required
def kategori_tambah():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip() or None
        slug = name.lower().replace(' ', '-')
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO categories (name, slug, description) VALUES (%s, %s, %s)",
                            (name, slug, description))
            conn.commit()
            flash('Kategori berhasil ditambahkan!', 'success')
            return redirect(url_for('admin.produk_list'))
        finally:
            conn.close()
    return render_template('admin/kategori_form.html', kategori=None)


@admin_bp.route('/kategori/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def kategori_edit(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM categories WHERE id = %s", (id,))
            kategori = cur.fetchone()
    finally:
        conn.close()
    if not kategori:
        flash('Kategori tidak ditemukan.', 'error')
        return redirect(url_for('admin.produk_list'))
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip() or None
        slug = name.lower().replace(' ', '-')
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("UPDATE categories SET name=%s, slug=%s, description=%s WHERE id=%s",
                            (name, slug, description, id))
            conn.commit()
            flash('Kategori berhasil diupdate!', 'success')
            return redirect(url_for('admin.produk_list'))
        finally:
            conn.close()
    return render_template('admin/kategori_form.html', kategori=kategori)


@admin_bp.route('/kategori/hapus/<int:id>', methods=['POST'])
@login_required
def kategori_hapus(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM categories WHERE id = %s", (id,))
        conn.commit()
        flash('Kategori berhasil dihapus.', 'success')
    except Exception:
        flash('Tidak bisa hapus kategori yang masih digunakan produk.', 'error')
    finally:
        conn.close()
    return redirect(url_for('admin.produk_list'))


# ── PRODUK LIST (dengan Kategori dalam Tab) ────────────────
@admin_bp.route('/produk')
@login_required
def produk_list():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT p.id, p.name, p.price, p.price_type, p.image, p.is_active,
                       c.name AS category
                FROM products p
                JOIN categories c ON p.category_id = c.id
                ORDER BY p.created_at DESC
            """)
            products = cur.fetchall()
            cur.execute("SELECT id, name, slug, description FROM categories ORDER BY name")
            categories = cur.fetchall()
    finally:
        conn.close()
    return render_template('admin/produk_list.html', products=products, categories=categories)


# ── PRODUK TAMBAH ──────────────────────────────────────────
@admin_bp.route('/produk/tambah', methods=['GET', 'POST'])
@login_required
def produk_tambah():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM categories ORDER BY name")
            categories = cur.fetchall()
    finally:
        conn.close()

    if request.method == 'POST':
        name        = request.form.get('name', '').strip()
        category_id = request.form.get('category_id')
        description = request.form.get('description', '').strip()
        price       = request.form.get('price', 0)
        price_type  = request.form.get('price_type') or None
        slug        = name.lower().replace(' ', '-')
        image_name  = None

        file = request.files.get('image')
        if file and allowed_file(file.filename):
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            filename   = secure_filename(file.filename)
            image_name = filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO products (category_id, name, slug, description, price, price_type, image, is_active)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, 1)
                """, (category_id, name, slug, description, price, price_type, image_name))
            conn.commit()
            flash('Produk berhasil ditambahkan!', 'success')
            return redirect(url_for('admin.produk_list'))
        finally:
            conn.close()

    return render_template('admin/produk_form.html', categories=categories, produk=None)


# ── PRODUK EDIT ────────────────────────────────────────────
@admin_bp.route('/produk/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def produk_edit(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM products WHERE id = %s", (id,))
            produk = cur.fetchone()
            cur.execute("SELECT id, name FROM categories ORDER BY name")
            categories = cur.fetchall()
    finally:
        conn.close()

    if not produk:
        flash('Produk tidak ditemukan.', 'error')
        return redirect(url_for('admin.produk_list'))

    if request.method == 'POST':
        name        = request.form.get('name', '').strip()
        category_id = request.form.get('category_id')
        description = request.form.get('description', '').strip()
        price       = request.form.get('price', 0)
        price_type  = request.form.get('price_type') or None
        is_active   = 1 if request.form.get('is_active') else 0
        slug        = name.lower().replace(' ', '-')
        image_name  = produk['image']

        file = request.files.get('image')
        if file and allowed_file(file.filename):
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            filename   = secure_filename(file.filename)
            image_name = filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE products
                    SET category_id=%s, name=%s, slug=%s, description=%s,
                        price=%s, price_type=%s, image=%s, is_active=%s
                    WHERE id=%s
                """, (category_id, name, slug, description, price, price_type, image_name, is_active, id))
            conn.commit()
            flash('Produk berhasil diupdate!', 'success')
            return redirect(url_for('admin.produk_list'))
        finally:
            conn.close()

    return render_template('admin/produk_form.html', categories=categories, produk=produk)


# ── PRODUK HAPUS ───────────────────────────────────────────
@admin_bp.route('/produk/hapus/<int:id>', methods=['POST'])
@login_required
def produk_hapus(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM products WHERE id = %s", (id,))
        conn.commit()
        flash('Produk berhasil dihapus.', 'success')
    finally:
        conn.close()
    return redirect(url_for('admin.produk_list'))


# ── GALERI LIST ────────────────────────────────────────────
@admin_bp.route('/galeri')
@login_required
def galeri_list():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM gallery ORDER BY created_at DESC")
            items = cur.fetchall()
    finally:
        conn.close()
    return render_template('admin/galeri_list.html', items=items)


# ── GALERI TAMBAH ──────────────────────────────────────────
@admin_bp.route('/galeri/tambah', methods=['GET', 'POST'])
@login_required
def galeri_tambah():
    if request.method == 'POST':
        type_ = request.form.get('type', 'photo')
        if type_ == 'testimonial':
            title = None
            desc = request.form.get('description', '').strip() or None
            author = request.form.get('author_name', '').strip() or None
            rating = int(request.form.get('rating')) if request.form.get('rating') else None
            image_name = None
        else:
            title = request.form.get('title', '').strip() or None
            desc = request.form.get('description_photo', '').strip() or None
            author = None
            rating = None
            image_name = None
            file = request.files.get('image')
            if file and allowed_file(file.filename):
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                filename = secure_filename(file.filename)
                image_name = filename
                file.save(os.path.join(UPLOAD_FOLDER, filename))

        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO gallery (type, title, description, image, author_name, rating, is_active)
                    VALUES (%s, %s, %s, %s, %s, %s, 1)
                """, (type_, title, desc, image_name, author, rating))
            conn.commit()
            flash('Item galeri berhasil ditambahkan!', 'success')
            return redirect(url_for('admin.galeri_list'))
        finally:
            conn.close()
    return render_template('admin/galeri_form.html', item=None)


# ── GALERI EDIT ────────────────────────────────────────────
@admin_bp.route('/galeri/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def galeri_edit(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM gallery WHERE id = %s", (id,))
            item = cur.fetchone()
    finally:
        conn.close()

    if not item:
        flash('Item tidak ditemukan.', 'error')
        return redirect(url_for('admin.galeri_list'))

    if request.method == 'POST':
        type_ = request.form.get('type', 'photo')
        if type_ == 'testimonial':
            title = None
            desc = request.form.get('description', '').strip() or None
            author = request.form.get('author_name', '').strip() or None
            rating = int(request.form.get('rating')) if request.form.get('rating') else None
            image_name = None
        else:
            title = request.form.get('title', '').strip() or None
            desc = request.form.get('description_photo', '').strip() or None
            author = None
            rating = None
            image_name = item['image']
            file = request.files.get('image')
            if file and allowed_file(file.filename):
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                filename = secure_filename(file.filename)
                image_name = filename
                file.save(os.path.join(UPLOAD_FOLDER, filename))

        is_active = 1 if request.form.get('is_active') else 0

        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE gallery SET type=%s, title=%s, description=%s,
                    image=%s, author_name=%s, rating=%s, is_active=%s WHERE id=%s
                """, (type_, title, desc, image_name, author, rating, is_active, id))
            conn.commit()
            flash('Item galeri berhasil diupdate!', 'success')
            return redirect(url_for('admin.galeri_list'))
        finally:
            conn.close()

    return render_template('admin/galeri_form.html', item=item)


# ── GALERI HAPUS ───────────────────────────────────────────
@admin_bp.route('/galeri/hapus/<int:id>', methods=['POST'])
@login_required
def galeri_hapus(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM gallery WHERE id = %s", (id,))
        conn.commit()
        flash('Item berhasil dihapus.', 'success')
    finally:
        conn.close()
    return redirect(url_for('admin.galeri_list'))


# ── FAQ LIST ───────────────────────────────────────────────
@admin_bp.route('/faq')
@login_required
def faq_list():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM faqs ORDER BY sort_order ASC")
            faqs = cur.fetchall()
    finally:
        conn.close()
    return render_template('admin/faq_list.html', faqs=faqs)


@admin_bp.route('/faq/tambah', methods=['GET', 'POST'])
@login_required
def faq_tambah():
    if request.method == 'POST':
        question   = request.form.get('question', '').strip()
        answer     = request.form.get('answer', '').strip()
        sort_order = request.form.get('sort_order', 0)
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO faqs (question, answer, sort_order) VALUES (%s, %s, %s)",
                            (question, answer, sort_order))
            conn.commit()
            flash('FAQ berhasil ditambahkan!', 'success')
            return redirect(url_for('admin.faq_list'))
        finally:
            conn.close()
    return render_template('admin/faq_form.html', faq=None)


@admin_bp.route('/faq/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def faq_edit(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM faqs WHERE id=%s", (id,))
            faq = cur.fetchone()
    finally:
        conn.close()
    if not faq:
        flash('FAQ tidak ditemukan.', 'error')
        return redirect(url_for('admin.faq_list'))
    if request.method == 'POST':
        question   = request.form.get('question', '').strip()
        answer     = request.form.get('answer', '').strip()
        sort_order = request.form.get('sort_order', 0)
        is_active  = 1 if request.form.get('is_active') else 0
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("UPDATE faqs SET question=%s, answer=%s, sort_order=%s, is_active=%s WHERE id=%s",
                            (question, answer, sort_order, is_active, id))
            conn.commit()
            flash('FAQ berhasil diupdate!', 'success')
            return redirect(url_for('admin.faq_list'))
        finally:
            conn.close()
    return render_template('admin/faq_form.html', faq=faq)


@admin_bp.route('/faq/hapus/<int:id>', methods=['POST'])
@login_required
def faq_hapus(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM faqs WHERE id=%s", (id,))
        conn.commit()
        flash('FAQ berhasil dihapus.', 'success')
    finally:
        conn.close()
    return redirect(url_for('admin.faq_list'))


# ── BLOG LIST ──────────────────────────────────────────────
@admin_bp.route('/blog')
@login_required
def blog_list():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT a.id, a.title, a.is_published, a.published_at, ad.username AS penulis
                FROM articles a JOIN admins ad ON a.admin_id = ad.id
                ORDER BY a.created_at DESC
            """)
            articles = cur.fetchall()
    finally:
        conn.close()
    return render_template('admin/blog_list.html', articles=articles)


# ── BLOG TAMBAH ────────────────────────────────────────────
@admin_bp.route('/blog/tambah', methods=['GET', 'POST'])
@login_required
def blog_tambah():
    if request.method == 'POST':
        title       = request.form.get('title', '').strip()
        content     = request.form.get('content', '').strip()
        excerpt     = request.form.get('excerpt', '').strip() or None
        is_pub      = 1 if request.form.get('is_published') else 0
        slug        = slugify(title)
        image_name  = None

        file = request.files.get('image')
        if file and allowed_file(file.filename):
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            filename   = secure_filename(file.filename)
            image_name = filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        conn = get_connection()
        try:
            with conn.cursor() as cur:
                from datetime import datetime
                pub_at = datetime.now() if is_pub else None
                cur.execute("""
                    INSERT INTO articles (admin_id, title, slug, content, excerpt, image, is_published, published_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (session['admin_id'], title, slug, content, excerpt, image_name, is_pub, pub_at))
            conn.commit()
            flash('Artikel berhasil ditambahkan!', 'success')
            return redirect(url_for('admin.blog_list'))
        finally:
            conn.close()
    return render_template('admin/blog_form.html', article=None)


# ── BLOG EDIT ──────────────────────────────────────────────
@admin_bp.route('/blog/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def blog_edit(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM articles WHERE id = %s", (id,))
            article = cur.fetchone()
    finally:
        conn.close()

    if not article:
        flash('Artikel tidak ditemukan.', 'error')
        return redirect(url_for('admin.blog_list'))

    if request.method == 'POST':
        title      = request.form.get('title', '').strip()
        content    = request.form.get('content', '').strip()
        excerpt    = request.form.get('excerpt', '').strip() or None
        is_pub     = 1 if request.form.get('is_published') else 0
        slug       = slugify(title)
        image_name = article['image']

        file = request.files.get('image')
        if file and allowed_file(file.filename):
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            filename   = secure_filename(file.filename)
            image_name = filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE articles SET title=%s, slug=%s, content=%s, excerpt=%s,
                    image=%s, is_published=%s, published_at=IF(%s=1 AND published_at IS NULL, NOW(), published_at)
                    WHERE id=%s
                """, (title, slug, content, excerpt, image_name, is_pub, is_pub, id))
            conn.commit()
            flash('Artikel berhasil diupdate!', 'success')
            return redirect(url_for('admin.blog_list'))
        finally:
            conn.close()

    return render_template('admin/blog_form.html', article=article)


# ── BLOG HAPUS ─────────────────────────────────────────────
@admin_bp.route('/blog/hapus/<int:id>', methods=['POST'])
@login_required
def blog_hapus(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM articles WHERE id = %s", (id,))
        conn.commit()
        flash('Artikel berhasil dihapus.', 'success')
    finally:
        conn.close()
    return redirect(url_for('admin.blog_list'))


# ── USER / ADMIN MANAGEMENT ────────────────────────────────
@admin_bp.route('/users')
@login_required
def user_list():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, username, email, created_at FROM admins ORDER BY created_at DESC")
            users = cur.fetchall()
    finally:
        conn.close()
    return render_template('admin/user_list.html', users=users)


@admin_bp.route('/users/tambah', methods=['GET', 'POST'])
@login_required
def user_tambah():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email    = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm  = request.form.get('confirm_password', '').strip()

        if not username or not email or not password:
            flash('Semua field harus diisi.', 'error')
            return render_template('admin/user_form.html', user=None)

        if password != confirm:
            flash('Password dan konfirmasi password tidak cocok.', 'error')
            return render_template('admin/user_form.html', user=None)

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO admins (username, email, password) VALUES (%s, %s, %s)",
                    (username, email, hashed.decode('utf-8'))
                )
            conn.commit()
            flash('Admin baru berhasil ditambahkan!', 'success')
            return redirect(url_for('admin.user_list'))
        except Exception as e:
            error_msg = str(e)
            if 'Duplicate' in error_msg:
                if 'username' in error_msg.lower():
                    flash('Username sudah digunakan.', 'error')
                elif 'email' in error_msg.lower():
                    flash('Email sudah digunakan.', 'error')
                else:
                    flash('Username atau email sudah digunakan.', 'error')
            else:
                flash('Gagal menambahkan admin: ' + error_msg, 'error')
            return render_template('admin/user_form.html', user=None)
        finally:
            conn.close()

    return render_template('admin/user_form.html', user=None)


@admin_bp.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def user_edit(id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, username, email FROM admins WHERE id = %s", (id,))
            user = cur.fetchone()
    finally:
        conn.close()

    if not user:
        flash('Admin tidak ditemukan.', 'error')
        return redirect(url_for('admin.user_list'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email    = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not email:
            flash('Username dan email harus diisi.', 'error')
            return render_template('admin/user_form.html', user=user)

        conn = get_connection()
        try:
            with conn.cursor() as cur:
                if password:
                    confirm = request.form.get('confirm_password', '').strip()
                    if password != confirm:
                        flash('Password dan konfirmasi password tidak cocok.', 'error')
                        return render_template('admin/user_form.html', user=user)
                    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                    cur.execute(
                        "UPDATE admins SET username=%s, email=%s, password=%s WHERE id=%s",
                        (username, email, hashed.decode('utf-8'), id)
                    )
                else:
                    cur.execute(
                        "UPDATE admins SET username=%s, email=%s WHERE id=%s",
                        (username, email, id)
                    )
            conn.commit()
            flash('Admin berhasil diupdate!', 'success')
            return redirect(url_for('admin.user_list'))
        except Exception as e:
            error_msg = str(e)
            if 'Duplicate' in error_msg:
                flash('Username atau email sudah digunakan.', 'error')
            else:
                flash('Gagal mengupdate admin: ' + error_msg, 'error')
            return render_template('admin/user_form.html', user=user)
        finally:
            conn.close()

    return render_template('admin/user_form.html', user=user)


@admin_bp.route('/users/hapus/<int:id>', methods=['POST'])
@login_required
def user_hapus(id):
    if id == session.get('admin_id'):
        flash('Tidak bisa menghapus akun sendiri.', 'error')
        return redirect(url_for('admin.user_list'))

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # Reassign articles to admin ID 1 before deleting
            cur.execute("UPDATE articles SET admin_id=1 WHERE admin_id=%s", (id,))
            cur.execute("DELETE FROM admins WHERE id=%s", (id,))
        conn.commit()
        flash('Admin berhasil dihapus.', 'success')
    except Exception as e:
        flash('Gagal menghapus admin: ' + str(e), 'error')
    finally:
        conn.close()
    return redirect(url_for('admin.user_list'))
