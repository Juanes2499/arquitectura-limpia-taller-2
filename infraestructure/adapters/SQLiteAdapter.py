import sqlite3

class SQLiteAdapter:
    def __init__(self):
        self.db_name = "SQLite.db"
        self.conn = sqlite3.connect("SQLite.db")
        self.cursor = self.conn.cursor()
        self._create_user_table()

    def _create_user_table(self):
        cursor = self.cursor
        conn = self.conn

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                password TEXT
            )
        ''')

        conn.commit()

    def excecuteQuery(self, query, parameters=None):

        cursor = self.cursor
        conn = self.conn

        try:
            if(parameters):
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)

        except sqlite3.Error as er:
            print(er)

        result = cursor.fetchall()

        conn.commit()

        return result
