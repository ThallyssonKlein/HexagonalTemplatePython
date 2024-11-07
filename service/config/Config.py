import os
from dotenv import load_dotenv

class ConfigError(Exception):
    pass

class Config:
    def __init__(self):
        load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

    def get_config(self):
        db_user = os.getenv('DB_USER')
        db_host = os.getenv('DB_HOST')
        db_name = os.getenv('DB_NAME')
        db_pass = os.getenv('DB_PASS')
        db_port = os.getenv('DB_PORT')

        if not all([db_user, db_host, db_name, db_pass, db_port]):
            raise ConfigError("One or more database configuration variables are missing")

        return {
            'db': {
                'user': db_user,
                'host': db_host,
                'database': db_name,
                'password': db_pass,
                'port': int(db_port)
            }
        }