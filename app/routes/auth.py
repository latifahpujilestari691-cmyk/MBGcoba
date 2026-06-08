from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.db import get_connection
import bcrypt

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Kalau sudah login, langsung ke dashboard
    if session.get('admin_id'):
        return redirect(url_for('admin.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id, username, password FROM admins WHERE username = %s", (username,))
                admin = cur.fetchone()
        finally:
            conn.close()

        if admin and bcrypt.checkpw(password.encode('utf-8'), admin['password'].encode('utf-8')):
            session['admin_id']   = admin['id']
            session['admin_name'] = admin['username']
            flash('Selamat datang, ' + admin['username'] + '!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Username atau password salah.', 'error')

    return render_template('admin/login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Berhasil logout.', 'success')
    return redirect(url_for('auth.login'))