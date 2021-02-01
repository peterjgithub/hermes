#!/bin/zsh

# ZSH SCRIPT INFO
# ****************
# zsh info: https://scriptingosx.com/2019/06/moving-to-zsh/

# set script OS file permissions:
# chmod u+x ./dbUpgrade.zsh
# chmod u+x ./dbmanager.py

# run script:
# ./dbUpgrade.zsh 

echo -n "This script will\n"
echo -n "apply all upgrade scripts to the db,\n"
echo -n "Type 5 if you are sure to continue "
read VAR

if [[ $VAR -eq 5 ]]
then
  python dbmanager.py db upgrade
fi



# FLASK MIGRATE INFO
# ******************
# Flask Migrate info: https://flask-migrate.readthedocs.io/en/latest/
# Flask Migrate sample: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

# 1) (only once) initialize Alembic (creates /migrations folder):
# python manage.py db init

# 2) (dev only) create our first migration script (/versions update):
# python manage.py db migrate

# 3) apply the upgrades to the database:    
# python manage.py db upgrade

