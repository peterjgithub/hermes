#!/bin/zsh

# ZSH SCRIPT INFO
# ****************
# zsh info: https://scriptingosx.com/2019/06/moving-to-zsh/

# set script OS file permissions:
# chmod u+x ././dbdbCreateScripts.zsh
# chmod u+x ./dbmanager.py

# run script in virtual environment with python3 and packages in requirements.txt installed:
# ./dbCreateScripts.zsh 

set -v
# This script will
# --> connect to the db,
# --> compare & identify updates,
# --> and create migration scripts.
set +v
echo -n "Type 5 if you are sure to continue "
read VAR

if [[ $VAR -eq 5 ]]
then
  set -v
  python dbmanager.py db migrate
fi