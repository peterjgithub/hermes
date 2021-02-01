#!/bin/zsh

# ZSH SCRIPT INFO
# ****************
# zsh info: https://scriptingosx.com/2019/06/moving-to-zsh/

# set script OS file permissions:
# chmod u+x ./dbUpgrade.zsh
# chmod u+x ./dbmanager.py

# run script in virtual environment with python3 and packages in requirements.txt installed:
# ./dbUpgrade.zsh 

set -v
# This script will
# --> apply all upgrade scripts to the db

set +v
echo -n "Type 5 if you are sure to continue "
read VAR

if [[ $VAR -eq 5 ]]
then
  set -v
  python dbmanager.py db upgrade
fi