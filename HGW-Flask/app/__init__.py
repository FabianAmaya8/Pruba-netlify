from flask import Flask
import psycopg2
import psycopg2.extras
from config import Config
from flask_cors import CORS

from .controllers.User.admin import admin_bp
from .controllers.User.mod import mod_bp
from .controllers.User.user import user_bp
from .controllers.User.login import login_bp
from .controllers.User.register import register_bp
from .controllers.User.catalogo import catalogo_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    dsn = (
        f"host={app.config['PG_HOST']} "
        f"user={app.config['PG_USER']} "
        f"password={app.config['PG_PASSWORD']} "
        f"dbname={app.config['PG_DB']} "
        f"port={app.config['PG_PORT']} "
        f"options='-c client_encoding=UTF8'"
    )

    try:
        connection = psycopg2.connect(
            dsn,
            cursor_factory=psycopg2.extras.RealDictCursor
        )
        app.config['PG_CONNECTION'] = connection
    except Exception as e:
        app.logger.error(f"❌ Error de conexión a PostgreSQL: {e}")
        raise

    # Registrar Blueprints
    app.register_blueprint(admin_bp)
    app.register_blueprint(mod_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(catalogo_bp)

    return app
