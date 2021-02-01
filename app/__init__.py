from flask import Flask
import os
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy import create_engine


print("\n" + "initiate __init__.py")

# App factory
def create_app(config_filename):
    """
    Initialise the core application context.
    """
    app = Flask(__name__, static_url_path='/static', template_folder='templates')
    app.config.from_object(config_filename)
    print_environment_variables(app)

    print("starting from app.models import db")
    from app.models import db

    with app.app_context():

        print("starting db.init_app(app)")
        db.init_app(app)

        print("starting configure_blueprints(app)")

        from app.home.route import home_bp
        app.register_blueprint(home_bp) 

        from app.tickers.route import tickers_bp
        app.register_blueprint(tickers_bp, url_prefix='/tickers') 
        
        from app.admin.route import admin_bp
        app.register_blueprint(admin_bp, url_prefix='/admin')

        print("finished configure_blueprints(app)")

    return app



def print_environment_variables(app):
    print("\n" + "****** Flask app.configs ******")
    print(f'ENVIRONMENT: {app.config["ENVIRONMENT"]}')
    print(f'ENV: {app.config["ENV"]}')
    print(f'DEBUG: {app.config["DEBUG"]}')
    print(f'TESTING: {app.config["TESTING"]}')
    print(f'PROPAGATE_EXCEPTIONS: {app.config["PROPAGATE_EXCEPTIONS"]}')
    print(f'PRESERVE_CONTEXT_ON_EXCEPTION: {app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]}')
    print(f'TRAP_HTTP_EXCEPTIONS: {app.config["TRAP_HTTP_EXCEPTIONS"]}')
    print(f'TRAP_BAD_REQUEST_ERRORS: {app.config["TRAP_BAD_REQUEST_ERRORS"]}')
    print(f'SECRET_KEY: {app.config["SECRET_KEY"]}')
    print(f'SESSION_COOKIE_NAME: {app.config["SESSION_COOKIE_NAME"]}')
    print(f'SESSION_COOKIE_DOMAIN: {app.config["SESSION_COOKIE_DOMAIN"]}')
    print(f'SESSION_COOKIE_PATH: {app.config["SESSION_COOKIE_PATH"]}')
    print(f'SESSION_COOKIE_HTTPONLY: {app.config["SESSION_COOKIE_HTTPONLY"]}')
    print(f'SESSION_COOKIE_SECURE: {app.config["SESSION_COOKIE_SECURE"]}')
    print(f'SESSION_COOKIE_SAMESITE: {app.config["SESSION_COOKIE_SAMESITE"]}')
    print(f'PERMANENT_SESSION_LIFETIME: {app.config["PERMANENT_SESSION_LIFETIME"]}')
    print(f'SESSION_REFRESH_EACH_REQUEST: {app.config["SESSION_REFRESH_EACH_REQUEST"]}')
    print(f'USE_X_SENDFILE: {app.config["USE_X_SENDFILE"]}')
    print(f'SEND_FILE_MAX_AGE_DEFAULT: {app.config["SEND_FILE_MAX_AGE_DEFAULT"]}')
    print(f'SERVER_NAME: {app.config["SERVER_NAME"]}')
    print(f'APPLICATION_ROOT: {app.config["APPLICATION_ROOT"]}')
    print(f'PREFERRED_URL_SCHEME: {app.config["PREFERRED_URL_SCHEME"]}')
    print(f'MAX_CONTENT_LENGTH: {app.config["MAX_CONTENT_LENGTH"]}')
    print(f'JSON_AS_ASCII: {app.config["JSON_AS_ASCII"]}')
    print(f'JSON_SORT_KEYS: {app.config["JSON_SORT_KEYS"]}')
    print(f'JSONIFY_PRETTYPRINT_REGULAR: {app.config["JSONIFY_PRETTYPRINT_REGULAR"]}')
    print(f'JSONIFY_MIMETYPE: {app.config["JSONIFY_MIMETYPE"]}')
    print(f'TEMPLATES_AUTO_RELOAD: {app.config["TEMPLATES_AUTO_RELOAD"]}')
    print(f'EXPLAIN_TEMPLATE_LOADING: {app.config["EXPLAIN_TEMPLATE_LOADING"]}')
    print(f'MAX_COOKIE_SIZE: {app.config["MAX_COOKIE_SIZE"]}')

    print("\n" + "****** CONFIGS IN hermes_config.py ******")
    print(f'POSTGRESQL_URL: {app.config["POSTGRESQL_URL"]}')
    print(f'SQLALCHEMY_DATABASE_URI: {app.config["SQLALCHEMY_DATABASE_URI"]}')
    print(f'SQLALCHEMY_TRACK_MODIFICATIONS: {app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]}')
    print(f'SQLALCHEMY_ECHO: {app.config["SQLALCHEMY_ECHO"]}')
    print(f'ALEMBIC_INI variable: {app.config["ALEMBIC_INI"]}')
    print(f'POLYGON_APIKEY: {app.config["POLYGON_APIKEY"]}')

    print("\n" + "****** .ENV CONFIGS ******")
    print("(fyi only - replace by app.config when needed to use")
    print(f'APP_SETTINGS: {os.getenv("APP_SETTINGS")}')
    print(f'FLASK_APP: {os.getenv("FLASK_APP")}')
    print(f'FLASK_ENV: {os.getenv("FLASK_ENV")}')
    print(f'FLASK_DEBUG: {os.getenv("FLASK_DEBUG")}')
    print(f'MONGO_PORT: {os.getenv("MONGO_PORT")}')
    print(f'MONGO_DBNAME: {os.getenv("MONGO_DBNAME")}')
    print(f'MONGO_COLLECTION: {os.getenv("MONGO_COLLECTION")}')
    print(f'MONGO_URL: {os.getenv("MONGO_URL")}')

if __name__ == '__main__':
    print("initiating __init__.py - __name__ == '__main__'")