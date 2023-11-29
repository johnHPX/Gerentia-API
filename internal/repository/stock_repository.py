import sqlite3
from internal.model import Estoque


class Estoque_Repository:
    def __init__(self, estoque_model: Estoque) -> None:
        self.conn = sqlite3.connect("internal/db/dat.db")
        self.model = estoque_model

    def backup(self, file_name) -> None:
        with open(file_name, 'w') as arquivo_sql:
            for linha in self.conn.iterdump():
                if 'INSERT INTO "tb_estoque"' in linha:
                    arquivo_sql.write('%s\n' % linha)

        self.conn.close()

    def store(self) -> Exception | None:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO tb_estoque (cod, nome, descricao, quantidade, preco_compra, preco_venda, data_atual, status, sincronizado) VALUES (?,?,?,?,?,?,?,?,?)", (self.model.cod, self.model.nome, self.model.descricao, self.model.quantidade, self.model.preco_compra, self.model.preco_venda, self.model.data_atual, self.model.status, 1))
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
                "UPDATE tb_estoque SET nome = ?, descricao = ?, quantidade = ?, preco_compra = ?, preco_venda = ?, status = ?, sincronizado = ? WHERE cod = ?", (self.model.nome, self.model.descricao, self.model.quantidade, self.model.preco_compra, self.model.preco_venda, self.model.status, 1, self.model.cod))
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
                "DELETE FROM tb_estoque WHERE cod = ?", (self.model.cod,)
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
                "SELECT * FROM tb_estoque"
            )

            for i in cursor.fetchall():
                obj = dict()
                obj['cod'] = i[0]
                obj['nome'] = i[1]
                obj['descricao'] = i[2]
                obj['quantidade'] = i[3]
                obj['preco_compra'] = i[4]
                obj['preco_venda'] = i[5]
                obj['data_atual'] = i[6]
                obj['hora_atual'] = i[7]
                obj['status'] = i[8]
                obj['sincronizado'] = i[9]
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
