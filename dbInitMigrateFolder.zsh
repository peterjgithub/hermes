#!/bin/zsh

# ZSH SCRIPT INFO
# ****************
# zsh info: https://scriptingosx.com/2019/06/moving-to-zsh/

# set script OS file permissions:
# chmod u+x ./dbInitMigrateFolder.zsh
# chmod u+x ./dbmanager.py

# run script:
# ./dbInitMigrateFolder.zsh 

echo -n "This script is initializing Alembic:\n"
echo -n "create a migration folder & scripts\n"
echo -n "This is very exceptional and should only happen once\n"
echo -n "type 5 if you are sure to continue "
read VAR

if [[ $VAR -eq 5 ]]
then
  python dbmanager.py db init
fi


# FLASK MIGRATE INFO
# ******************
# Flask Migrate info: https://flask-migrate.readthedocs.io/en/latest/
# Flask Migrate sample: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

# 1) (only once) initialize Alembic (creates /migrations folder):


# 2) (dev only) create our first migration script (/versions update):
# python manage.py db migrate

# 3) apply the upgrades to the database:    
# python manage.py db upgrade

