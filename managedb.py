import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv
from app import app, db

print("initiate manage.py")

# info: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

# 1) initialize Alembic (creates /migrations folder):
# (only once)
# python manage.py db init

# 2) create our first migration script (/versions update):
# python manage.py db migrate

# 3) apply the upgrades to the database:
# python manage.py db upgrade

migrate = Migrate(app, db)
print("finished: migrate = Migrate(app, db)")

manager = Manager(app)
print("finished: manager = Manager(app)")

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    print("initiate manage.py __name__ = __main__")
    manager.run()
