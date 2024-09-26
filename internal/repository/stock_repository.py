import sqlite3
from internal.model import Estoque


class Estoque_Repository:
    def __init__(self, estoque_model: Estoque) -> None:
        self.model = estoque_model

    def start_conection(self):
        self.conn = sqlite3.connect("internal/db/gerentia.db")

    def close_connection(self):
        self.conn.close()

    def backup(self, file_name) -> None:
        self.start_conection()
        with open(file_name, "w") as arquivo_sql:
            for linha in self.conn.iterdump():
                if 'INSERT INTO "tb_estoque"' in linha:
                    arquivo_sql.write("%s\n" % linha)
        self.close_connection()

    def verific_stock_exists(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"SELECT * FROM {'tb_estoque'} WHERE cod = ?", (self.model.cod,)
            )
            rows = cursor.fetchall()
        except Exception as error:
            cursor.close()
            return Exception(101, error.args[0])
        else:
            cursor.close()
            self.conn.commit()
            if len(rows) == 1:
                return True
            else:
                return False

    def store(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"INSERT INTO {'tb_estoque'} (cod, nome, descricao, quantidade, preco_compra, preco_venda, data_atual,hora_atual, status, sincronizado) VALUES (?,?,?,?,?,?,?,?,?,?)",
                (
                    self.model.cod,
                    self.model.nome,
                    self.model.descricao,
                    self.model.quantidade,
                    self.model.preco_compra,
                    self.model.preco_venda,
                    self.model.data_atual,
                    self.model.hora_atual,
                    self.model.status,
                    1,
                ),
            )
        except Exception as error:
            cursor.close()
            return Exception(102, error.args[0])
        else:
            cursor.close()
            self.conn.commit()
            return None

    def edit(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"UPDATE {'tb_estoque'} SET nome = ?, descricao = ?, quantidade = ?, preco_compra = ?, preco_venda = ?, status = ?, sincronizado = ? WHERE cod = ?",
                (
                    self.model.nome,
                    self.model.descricao,
                    self.model.quantidade,
                    self.model.preco_compra,
                    self.model.preco_venda,
                    self.model.status,
                    1,
                    self.model.cod,
                ),
            )
        except Exception as error:
            cursor.close()
            return Exception(103, error.args[0])
        else:
            cursor.close()
            self.conn.commit()
            return None

    def remove(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"DELETE FROM {'tb_estoque'} WHERE cod = ?", (self.model.cod,)
            )
        except Exception as error:
            cursor.close()
            return Exception(104, error.args[0])
        else:
            cursor.close()
            self.conn.commit()
            return None

    def list(self):
        dto = list()
        self.start_conection()
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {'tb_estoque'}")

            for i in cursor.fetchall():
                obj = dict()
                obj["cod"] = i[0]
                obj["nome"] = i[1]
                obj["descricao"] = i[2]
                obj["quantidade"] = i[3]
                obj["preco_compra"] = i[4]
                obj["preco_venda"] = i[5]
                obj["data_atual"] = i[6]
                obj["hora_atual"] = i[7]
                obj["status"] = i[8]
                obj["sincronizado"] = i[9]
                dto.append(obj)

        except Exception as error:
            cursor.close()
            return Exception(105, error.args[0])
        else:
            cursor.close()
            self.conn.commit()
            return dto
