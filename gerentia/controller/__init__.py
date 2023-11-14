import sqlite3
import io

def create_db(app):
    with open("migrations/schemas_db.sql") as f:
        contents = f.readlines()
    conn = sqlite3.connect("dat.db")
    cursor = conn.cursor()
    cursor.execute(contents)
    conn.commit()
    conn.close()


def compare_db(app):
    pass


def update_db(schemas):
    conn = sqlite3.connect("dat.db")
    cursor = conn.cursor()
    cursor.execute("")
    conn.commit()
    conn.close()


def backup_db():
    conn = sqlite3.connect('dat.db')
    # Open() function
    with io.open('backup/backupDB_dump.sql', 'w') as p:
        # iterdump() function
        for line in conn.iterdump():
            p.write('%s\n' % line)
    print('Backup performed successfully!')
    print('Data Saved as backupdatabase_dump.sql')
    conn.close() 


def synchronize_db():
    backup_db()

    with open("backup/backupDB_dump.sql") as f:
        schemas = f.readlines()
    
    return schemas