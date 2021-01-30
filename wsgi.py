from app import init_app
import os

print("start wsgi.py")

environment = os.getenv('ENVIRONMENT', 'development').capitalize()
config_file = f"hermes_config.{environment}"
# config_file = f"hermes_config.Development"

print(f"launching init_app({config_file})")
app = init_app(config_file)

if __name__ == "__main__":
    print("initiate wsgi.py - if __name__ ==__main__")
    app.run()