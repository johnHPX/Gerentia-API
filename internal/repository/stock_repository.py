import sqlite3
from internal.model import Estoque


class Estoque_Repository:
    def __init__(self, estoque_model: Estoque) -> None:
        self.conn = sqlite3.connect("internal/db/dat.db")
        self.model = estoque_model

    def store(self) -> Exception | None:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO tb_estoque (cod, nome, descricao, quantidade, preco_compra, preco_venda, data_atual, status, sincronizado) VALUES (?,?,?,?,?,?,?,?,?)", (self.model.cod, self.model.nome, self.model.descricao, self.model.quantidade, self.model.preco_compra, self.model.preco_venda, self.model.data_atual, self.model.status, 1))
        except Exception as error:
            cursor.close()
            self.conn.commit()
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
            self.conn.commit()
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
            self.conn.commit()
            self.conn.close()
            return error
        else:
            cursor.close()
            self.conn.commit()
            self.conn.close()
            return None
