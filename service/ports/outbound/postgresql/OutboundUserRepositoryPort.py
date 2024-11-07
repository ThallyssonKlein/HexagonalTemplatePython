from psycopg2 import pool
from typing import List, Dict

class OutboundUserRepositoryPort:

    def __init__(self, database: pool.SimpleConnectionPool):
        self.database = database

    def find_user_by_username(self, username: str) -> List[Dict]:
        with self.database.getconn() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM users WHERE username = %s AND is_deleted = FALSE', (username,))
                return cursor.fetchall()

    def find_user_by_id(self, user_id: int) -> List[Dict]:
        with self.database.getconn() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM users WHERE id = %s AND is_deleted = FALSE', (user_id,))
                return cursor.fetchall()