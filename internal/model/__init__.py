import sqlite3


class Database_Model:
    def __init__(self, db_src):
        self.conn = sqlite3.connect(db_src)

    def get_conn(self):
        return self.conn

    def closer_conn(self):
        self.conn.commit()
        self.conn.close()


def new_database_model(db_src):
    return Database(db_src)
