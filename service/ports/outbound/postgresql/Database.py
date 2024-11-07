import psycopg2
from psycopg2 import pool
from config import Config

class Database:
    _instance = None

    def __init__(self):
        self._pool = None

    def connect(self):
        config = Config().get_config()
        self._pool = psycopg2.pool.SimpleConnectionPool(
            1, 20,
            user=config['db']['user'],
            password=config['db']['password'],
            host=config['db']['host'],
            port=config['db']['port'],
            database=config['db']['database']
        )

    @staticmethod
    def get_instance():
        if Database._instance is None:
            Database._instance = Database()
        return Database._instance

    def get_pool(self):
        return self._pool