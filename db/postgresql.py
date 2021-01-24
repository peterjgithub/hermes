from dotenv import load_dotenv
import os
load_dotenv()

_database_url = os.getenv("DATABASE_URL")
if _database_url == None:
    template = "postgres://{user}:{pwd}@{server}:{port}/{db}"
    _database_url = template.format(
        user=os.getenv("POSTGRESQL_USER"),
        pwd=os.getenv("POSTGRESQL_PWD"),
        server=os.getenv("POSTGRESQL_SERVER"),
        port=os.getenv("POSTGRESQL_PORT"),
        db=os.getenv("DATABASE_URL"),
    )

