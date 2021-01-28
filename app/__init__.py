from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

print("\n" + "initiate __init__.py")

load_dotenv()
app = Flask(__name__)

print(f"OS var ENVIRONMENT={os.getenv('ENVIRONMENT')}")

ENVIRONMENT = os.getenv('ENVIRONMENT')
print(f'ENVIRONMENT={ENVIRONMENT}')

if ENVIRONMENT == 'production':
    print("loading configs from hermes_config.ProductionConfig")
    app.config.from_object('hermes_config.ProductionConfig')

if ENVIRONMENT == 'development':
    print("loading configs from hermes_config.DevelopmentConfig")
    app.config.from_object('hermes_config.DevelopmentConfig')

print("\n" + "****** Flask app.config ******")
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


# sqlalchemy_db_uri = os.getenv("SQLALCHEMY_DATABASE_URI") 
# engine = SQLAlchemy.create_engine(sqlalchemy_db_uri)
# alembic_cfg = os.getenv("ALEMBIC_INI")
# script_ = script.ScriptDirectory.from_config(alembic_cfg)
# with engine.begin() as conn:
#     context = migration.MigrationContext.configure(conn)
#     if context.get_current_revision() != script_.get_current_head():

#     	migrate = Migrate(app, db)
# 		manager = Manager(app)
# 		manager.add_command('db', MigrateCommand)

#         raise exceptions.DatabaseIsNotUpToDate('Upgrade the database.')

db = SQLAlchemy(app)
# use multiple databases: https://turbogears.readthedocs.io/en/latest/cookbook/multiple-databases.html

from app import views
from app import models