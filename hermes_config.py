# REQUIRED 
# as OS environment variables
# or as defined in .env file:
# ************************************

# FLASK_APP=runner.py
# FLASK_ENV=development
# FLASK_DEBUG=1
# needed in .env to launch in development with commmand
# flask run

# ENVIRONMENT=production,development
# is used to select the correct (non secret) configs to inject

# SECRET_KEY=[string]
# is a secret key used to keep the client-side sessions secure 
# keep it very secret!

# POLYGON_APIKEY=[key]
# is secret api key to use polygon.io (better use a different key in production)

# POSTGRESQL_URL=[full connection string]
# is the secret connection string needed for postgresql db
#   DATABASE_URL=overwrites POSTGRESQL_URL in production (digitalocean standard)
#   POSTGRESQL_URL is pushed to app.config SQLALCHEMY_DATABASE_URI

import os

from dotenv import load_dotenv
load_dotenv()

print("initiate hermes_config.py")

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    print(f"initiate class BaseConfig({object})")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development").lower()
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    POLYGON_APIKEY = os.getenv("POLYGON_APIKEY")
    ALEMBIC_MIGRATIONS_FOLDER = 'migrations'
    ALEMBIC_INI = os.path.join(basedir, 'migrations', 'alembic.ini')
    SECRET_KEY = os.getenv("SECRET_KEY")

    # APP_SETTINGS=os.getenv("APP_SETTINGS")


class Development(BaseConfig):
    print("initiate class DevelopmentConfig(BaseConfig)")
    DEVELOPMENT = True
    DEBUG = True
    POSTGRESQL_URL = os.getenv("POSTGRESQL_URL")
    SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRESQL_URL")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(BaseConfig):
    print("initiate class ProductionConfig(BaseConfig)")
    DEVELOPMENT = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    POSTGRESQL_URL = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


# class StagingCfg(BaseCfg):
#     DEVELOPMENT = True
#     DEBUG = True


# class TestingCfg(BaseCfg):
#     TESTING = True

# https://gist.github.com/m-aciek/118d450ee59a41176214b5f93a02cc6f

# from alembic import config
# from alembic import script
# from alembic.runtime import migration
# import sqlalchemy

# import exceptions


# engine = sqlalchemy.create_engine(DATABASE_URL)
# alembic_cfg = config.Config('alembic.ini')
# script_ = script.ScriptDirectory.from_config(alembic_cfg)
# with engine.begin() as conn:
#     context = migration.MigrationContext.configure(conn)
#     if context.get_current_revision() != script_.get_current_head():
#         raise exceptions.DatabaseIsNotUpToDate('Upgrade the database.')