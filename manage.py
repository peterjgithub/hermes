import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv
from app import app, db

# info: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

# 1) initialize Alembic (creates /migrations folder):
# (only once)
# python manage.py db init

# 2) create our first migration script (/versions update):
# python manage.py db migrate

# 3) apply the upgrades to the database:
# python manage.py db upgrade


load_dotenv()
print("manage.py")
FLASK_ENV = os.getenv('FLASK_ENV')
print(f"FLASK_ENV = {FLASK_ENV}")

# app.config.from_object(os.environ['APP_SETTINGS'])
ENVIRONMENT = os.getenv('ENVIRONMENT')
print(f"ENVIRONMENT = {ENVIRONMENT}")

if ENVIRONMENT == 'production':
    app.config.from_object('hermes_config.ProductionConfig')
    DEVELOPMENT = os.getenv('DEVELOPMENT')
    print(f"DEVELOPMENT = {DEVELOPMENT}")

if ENVIRONMENT == 'development':
    app.config.from_object('hermes_config.DevelopmentConfig')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    print(f"SQLALCHEMY_TRACK_MODIFICATIONS = {SQLALCHEMY_TRACK_MODIFICATIONS}")

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
