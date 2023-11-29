import sqlite3
from internal.model import Vendas


class Vendas_Repository:
    def __init__(self, sales_model: Vendas) -> None:
        self.conn = sqlite3.connect("internal/db/gerentia.db")
        self.model = sales_model

    def backup(self, file_name) -> None:
        with open(file_name, 'w') as arquivo_sql:
            for linha in self.conn.iterdump():
                if 'INSERT INTO "tb_vendas"' in linha:
                    arquivo_sql.write('%s\n' % linha)

        self.conn.close()

    def store(self) -> Exception | None:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"INSERT INTO {'tb_vendas'} (id, nome, quantidade, valor, total, data, status, sincronizado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (self.model.id, self.model.nome, self.model.quantidade, self.model.valor, self.model.total, self.model.data, self.model.status, 1))
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
                f"UPDATE {'tb_vendas'} SET nome = ?, quantidade = ?, valor = ?, total = ?, status = ?, sincronizado = ? WHERE id = ?", (self.model.nome, self.model.quantidade, self.model.valor, self.model.total, self.model.status, 1, self.model.id))
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
                f"DELETE FROM {'tb_vendas'} WHERE id = ?", (self.model.id,)
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
                f"SELECT * FROM {'tb_vendas'}"
            )

            for i in cursor.fetchall():
                obj = dict()
                obj['id'] = i[0]
                obj['nome'] = i[1]
                obj['quantidade'] = i[2]
                obj['valor'] = i[3]
                obj['total'] = i[4]
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
