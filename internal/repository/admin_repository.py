import sqlite3
from internal.model.funcionarios import Funcionarios


class Admin_Repository:
    def __init__(self, model_admin: Funcionarios) -> None:
        self.conn = sqlite3.connect("internal/db/dat.db")
        self.model = model_admin

    def backup(self, file_name) -> None:
        with open(file_name, 'w') as arquivo_sql:
            for linha in self.conn.iterdump():
                if 'INSERT INTO "tb_funcionarios"' in linha:
                    arquivo_sql.write('%s\n' % linha)
        self.conn.close()

    def store(self) -> Exception | None:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"INSERT INTO {'tb_funcionarios'} (matricula, nome, cargo, nome_usuario, senha, data_atual, hora_atual, status, sincronizado) VALUES (?,?,?,?,?,?,?,?,?)", (self.model.matricula, self.model.nome, self.model.cargo, self.model.nome_usuario, self.model.senha, self.model.data_atual, self.model.hora_atual, self.model.status, self.model.sincronizado))
        except Exception as error:
            cursor.close()
            self.conn.close()
            return error
        else:
            cursor.close()
            self.conn.commit()
            self.conn.close()
            return None

    def edit(self) -> Exception | None:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"UPDATE {'tb_funcionarios'} SET nome = ?, cargo = ?, nome_usuario = ?, senha = ?, data_atual = ?, hora_atual = ?, status = ?, sincronizado = ? WHERE matricula = ?", (self.model.nome, self.model.cargo, self.model.nome_usuario, self.model.senha, self.model.data_atual, self.model.hora_atual, self.model.status, self.model.sincronizado, self.model.matricula))
        except Exception as error:
            cursor.close()
            self.conn.close()
            return error
        else:
            cursor.close()
            self.conn.commit()
            self.conn.close()
            return None

    def remove(self) -> Exception | None:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"DELETE FROM {'tb_funcionarios'} WHERE matricula = ?", (
                    self.model.matricula,)
            )
        except Exception as error:
            cursor.close()
            self.conn.close()
            return error
        else:
            cursor.close()
            self.conn.commit()
            self.conn.close()
            return None

    def list(self) -> list[dict] | Exception:
        dto = list()
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"SELECT * FROM {'tb_funcionarios'}"
            )

            for i in cursor.fetchall():
                obj = dict()
                obj['matricula'] = i[0]
                obj['nome'] = i[1]
                obj['cargo'] = i[2]
                obj['nome_usuario'] = i[3]
                obj['senha'] = i[4]
                obj['data_atual'] = i[5]
                obj['hora_atual'] = i[6]
                obj['status'] = i[7]
                obj['sincronizado'] = i[8]
                dto.append(obj)

        except Exception as error:
            cursor.close()
            self.conn.close()
            return error
        else:
            cursor.close()
            self.conn.commit()
            self.conn.close()
            return dto
