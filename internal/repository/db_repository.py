import sqlite3
import io


class Database_Repository:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("internal/db/gerentia.db")

    def backup_db(self):
        try:
            with io.open('internal/backup/backupDB_dump.sql', 'w') as p:
                for line in self.conn.iterdump():
                    p.write('%s\n' % line)
        except Exception as e:
            print(e)
        else:
            print('Backup performed successfully!')
            print('Data Saved as backupdatabase_dump.sql')
        finally:
            self.conn.close()
