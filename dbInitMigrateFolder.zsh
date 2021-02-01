#!/bin/zsh

# ZSH SCRIPT INFO
# ****************
# zsh info: https://scriptingosx.com/2019/06/moving-to-zsh/

# set script OS file permissions:
# chmod u+x ./dbInitMigrateFolder.zsh
# chmod u+x ./dbmanager.py

# run script in virtual environment with python3 and packages in requirements.txt installed:
# ./dbInitMigrateFolder.zsh 

set -v
# This script is initializing Alembic:
# --> create a migration folder & scripts
# "This is very exceptional and should only happen once
set +v
echo -n "type 5 if you are sure to continue "
read VAR

if [[ $VAR -eq 5 ]]
then
  set -v
  python dbmanager.py db init
fi


