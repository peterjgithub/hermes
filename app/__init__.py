from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
print("__init__.py")
app = Flask(__name__)

ENVIRONMENT = os.getenv('ENVIRONMENT')
if ENVIRONMENT == 'production':
    app.config.from_object('hermes_config.ProductionConfig')
if ENVIRONMENT == 'development':
    app.config.from_object('hermes_config.DevelopmentConfig')

print(f'ENV variable is set to: {app.config["ENV"]}')

db = SQLAlchemy(app)

from app import views
from app import models