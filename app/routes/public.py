from flask import Blueprint, render_template, request, abort
from app.models.db import get_connection

public_bp = Blueprint('public', __name__)


@public_bp.route('/')
def index():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, title, image
                FROM gallery
                WHERE type = 'photo' AND is_active = 1
                ORDER BY created_at DESC LIMIT 6
            """)
            photos = cur.fetchall()
            cur.execute("""
                SELECT author_name, description, rating, image
                FROM gallery
                WHERE type = 'testimonial' AND is_active = 1
                ORDER BY created_at DESC LIMIT 3
            """)
            testimoni = cur.fetchall()
            cur.execute("""
                SELECT p.id, p.slug, p.name, p.price, p.price_type, p.image,
                       c.name AS category
                FROM products p
                JOIN categories c ON p.category_id = c.id
                WHERE p.is_active = 1
                ORDER BY p.created_at DESC LIMIT 3
            """)
            featured_products = cur.fetchall()
    finally:
        conn.close()
    return render_template('index.html', photos=photos, testimoni=testimoni, featured_products=featured_products)


@public_bp.route('/tentang')
def tentang():
    return render_template('tentang.html')


@public_bp.route('/galeri')
def galeri():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, title, description, image
                FROM gallery
                WHERE type = 'photo' AND is_active = 1
                ORDER BY created_at DESC
            """)
            photos = cur.fetchall()

            cur.execute("""
                SELECT author_name, image, description, rating
                FROM gallery
                WHERE type = 'testimonial' AND is_active = 1
                ORDER BY created_at DESC
            """)
            testimoni = cur.fetchall()
    finally:
        conn.close()

    return render_template('galeri.html', photos=photos, testimoni=testimoni)


@public_bp.route('/produk')
def produk():
    keyword  = request.args.get('q', '').strip()
    category = request.args.get('category', '').strip()

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, slug FROM categories ORDER BY name")
            categories = cur.fetchall()

            sql = """
                SELECT p.id, p.slug, p.name, p.price, p.price_type, p.image,
                       c.name AS category, c.slug AS category_slug
                FROM products p
                JOIN categories c ON p.category_id = c.id
                WHERE p.is_active = 1
            """
            params = []

            if keyword:
                sql += " AND p.name LIKE %s"
                params.append(f"%{keyword}%")

            if category:
                sql += " AND c.slug = %s"
                params.append(category)

            sql += " ORDER BY p.created_at DESC"
            cur.execute(sql, params)
            products = cur.fetchall()

    finally:
        conn.close()

    return render_template('produk.html',
                           products=products,
                           categories=categories,
                           keyword=keyword,
                           category=category)


@public_bp.route('/produk/<slug>')
def produk_detail(slug):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT p.id, p.name, p.price, p.price_type, p.image, p.description,
                       c.name AS category, c.slug AS category_slug
                FROM products p
                JOIN categories c ON p.category_id = c.id
                WHERE p.slug = %s AND p.is_active = 1
            """, (slug,))
            product = cur.fetchone()
            if not product:
                abort(404)
    finally:
        conn.close()

    return render_template('produk_detail.html', product=product)


@public_bp.route('/faq')
def faq():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT question, answer FROM faqs WHERE is_active=1 ORDER BY sort_order ASC")
            faqs = cur.fetchall()
    finally:
        conn.close()
    return render_template('faq.html', faqs=faqs)


@public_bp.route('/blog')
def blog():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, title, slug, excerpt, image, published_at
                FROM articles
                WHERE is_published = 1
                ORDER BY published_at DESC
            """)
            articles = cur.fetchall()
    finally:
        conn.close()

    return render_template('blog.html', articles=articles)


@public_bp.route('/blog/<slug>')
def blog_detail(slug):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT a.id, a.title, a.content, a.image,
                       a.published_at, ad.username AS penulis
                FROM articles a
                JOIN admins ad ON a.admin_id = ad.id
                WHERE a.slug = %s AND a.is_published = 1
            """, (slug,))
            article = cur.fetchone()

            if not article:
                abort(404)

            cur.execute("""
                SELECT title, slug, published_at
                FROM articles
                WHERE is_published = 1 AND slug != %s
                ORDER BY published_at DESC
                LIMIT 4
            """, (slug,))
            other_articles = cur.fetchall()

    finally:
        conn.close()

    return render_template('blog_detail.html',
                           article=article,
                           other_articles=other_articles)