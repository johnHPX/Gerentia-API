import sqlite3
import io


class Database_Controller:
    def __init__(self) -> None:
        pass


def new_database_controller():
    return Database_Controller()


def backup_db():
    conn = sqlite3.connect('dat.db')
    with io.open('backup/backupDB_dump.sql', 'w') as p:
        for line in conn.iterdump():
            p.write('%s\n' % line)
    print('Backup performed successfully!')
    print('Data Saved as backupdatabase_dump.sql')
    conn.close()


'''
    Functions Precises
'''


def query_db(sql_command):
    conn = sqlite3.connect('dat.db')
    cursor = conn.cursor()
    cursor.execute(sql_command)
    conn.commit()
    conn.close()


def synchronize_db(obj):
    backup_db()
    if obj['sincronizado'] == 0:
        if obj['status'] == 0:
            sql_command = f'''
                INSERT INTO tb_funcionarios (matricula, nome, cargo, nome_usuario, senha, status, sincronizado) VALUES ({obj['matricula']}, "{obj['nome']}", "{obj['cargo']}", "{obj['nome_usuario']}", "{obj['senha']}",{obj['status']}, {1})
            '''

            query_db(sql_command)
        elif obj['status'] == 1:
            pass
        elif obj['status'] == 2:
            pass
