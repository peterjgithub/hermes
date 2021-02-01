from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

print("initiate dbmanager.py")

# print("start db = SQLAlchemy()")
# db = SQLAlchemy()

# def create_app():

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
from app.models import Quote
print(f"starting from app.models import TestObject")
from app.models import TestObject

    # any other registrations; blueprints, template utilities, commands
    # print(f"finished call - return app")
    # return app

# if __name__ == '__main__':
#     print("initiating __init__.py - __name__ == '__main__'")
#     print("from __name__ launching create_app()")
#     create_app()

if __name__ == '__main__':
    manager.run()