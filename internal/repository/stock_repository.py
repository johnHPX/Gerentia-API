import sqlite3


class Estoque_Repository:
    def __init__(self, estoque_model) -> None:
        self.conn = sqlite3.connect("internal/db/dat.db")
        self.model = estoque_model

    def store(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO tb_estoque (cod, nome, descricao, quantidade, preco_compra, preco_venda, data_atual, status, sincronizado) VALUES (?,?,?,?,?,?,?,?,?)", (self.model.cod, self.model.nome, self.model.descricao, self.model.quantidade, self.model.preco_compra, self.model.preco_venda, self.model.data_atual, self.model.status, 1))
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            self.conn.commit()
            self.conn.close()
