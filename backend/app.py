import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_migrate import Migrate
from werkzeug.security import check_password_hash, generate_password_hash
from config import config_by_name
from models import User, db

migrate = Migrate()


def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    db.init_app(app)
    migrate.init_app(app, db)
    return app


app = create_app(os.environ.get('.env', 'dev'))


@app.route('/')
def index():
    if 'user_id' in session:
        if session.get('role') == 'admin':
            return redirect(url_for('admin.menu'))
        return redirect(url_for('customer.catalog'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password') or ''
            email = request.form.get('email')
            name = request.form.get('name')
            role = request.form.get('role', 'customer')

            if User.query.filter_by(username=username).first():
                flash('Username already exists.', 'error')
                return redirect(url_for('login'))

            new_user = User()
            new_user.username = username
            new_user.password_hash = generate_password_hash(password)
            new_user.role = role
            new_user.email = email
            new_user.name = name

            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))

        except Exception as e:
            print(f"Error during registration: {e}")
            db.session.rollback()
            flash('Cannot register user.', 'error')
    return render_template('/register.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=5000)
