import os
from flask import Flask
from flask_migrate import Migrate
from config import config_by_name
from models import db

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
    return "Welcome to the Meal Ordering System API!"


if __name__ == '__main__':
    app.run(port=5000)