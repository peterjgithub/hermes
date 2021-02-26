# hermes
stock exchanges, quotes, technical analysis, etc


## Usage

create virtual environment:
```
python3 -m venv venv
```

starting flask app in dev:
```
source venv/bin/activate
flask run
```

(or . venv/bin/activate)

when finished: stop flask (ctrl+c) and terminate venv:
```
deactivate
```


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install hermes.

```bash
pip3 install --upgrade xxx
```
see requirements.txt to install all packages

generate requirements.txt:
```
pip3 freeze > requirements.txt
```

to upgrade pip to the latest version:
```
/Users/peter/GitHub/hermes/venv/bin/python3 -m pip3 install --upgrade pip
```
list all outdated packages (eg in venv):
```
pip3 list --outdated                                                     
```

to update all venv packages according to requirements.txt
```
pip3 install --upgrade -r requirements.txt
```

My last python version:
/opt/homebrew/opt/python@3.9/libexec/bin

## application structure

/hermes
    /app
        __init__.py
        /static
        /templates
        views.py
    config.py
    runner.py


/hermes
=> The app_dir is the root directory of the Flask project.

/hermes/config.py	
=> The config.py contains settings and configuration for the Flask application.

/hermes/runner.py	
=> The entry point for your Flask application.

/hermes/app	
=> The app directory is a Python package which holds views, templates, and static files.

/hermes/app/__init__.py	
=> The __init__.py tells the Python that app directory is a Python package.

/hermes/app/static	
=> The static directory contains the static files of the project.

/hermes/app/templates	
=> The templates directory contains templates.

/hermes/app/views.py	
=> The views.py contains routes and view functions.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Name orgin

Hermes was the ancient Greek god of trade, wealth, luck, fertility, animal husbandry, sleep, language, thieves, and travel. 

One of the cleverest and most mischievous of the Olympian gods, he was the patron of shepherds, invented the lyre, and was, above all, the herald and messenger of Mt. Olympus so that he came to symbolise the crossing of boundaries in his role as a guide between the two realms of gods and humanity.

https://en.wikipedia.org/wiki/Hermes
