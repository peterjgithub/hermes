from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

print("initiate dbmanager.py")

print("start app = Flask(__name__)")
app = Flask(__name__)

environment = os.getenv('ENVIRONMENT', 'development').capitalize()
config_file = f"hermes_config.{environment}"
print(f"start app.config.from_object({config_file})")
app.config.from_object(config_file)
print(f"app.config['SQLALCHEMY_DATABASE_URI'] = {app.config['SQLALCHEMY_DATABASE_URI']}")

print(f"starting db.init_app(app)")
from app.models import db
db.init_app(app)

print(f"starting Migrate(app, db)")
Migrate(app, db)

print(f"starting manager = Manager(app)")
manager = Manager(app)

print(f"starting manager.add_command('db', MigrateCommand)")
manager.add_command('db', MigrateCommand)

# importing the models to make sure they are known to Flask-Migrate
print(f"starting from app.models import Quote")
from app import models

if __name__ == '__main__':
    manager.run()

# FLASK MIGRATE INFO
# ******************
# Flask Migrate info: https://flask-migrate.readthedocs.io/en/latest/
# Flask Migrate sample: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

# 1) (only once) initialize Alembic (creates /migrations folder)
# python dbmanager.py db init
# or run ./dbInitMigrateFolders.zsh

# 2) (dev only) create our first migration script (/versions update):
# python manage.py db migrate
# or run ./dbCreateScripts.zsh

# 3) apply the upgrades to the database:    
# python manage.py db upgrade
# or run ./dbUpgrade.zsh