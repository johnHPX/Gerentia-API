import internal.repository as repository
from internal.model import Estoque


class Estoque_Controller:
    def __init__(self, estoque_model: Estoque) -> None:
        self.model = estoque_model

    def backup_db(self):
        db_rep = repository.new_db_repository()
        db_rep.backup_db()

    def synchronize(self):
        self.backup_db()
        if self.model.sincronizado == 0:
            if self.model.status == 0:
                stock_rep = repository.new_stock_repository(self.model)
                return stock_rep.store()
            elif self.model.status == 1:
                stock_rep = repository.new_stock_repository(self.model)
                return stock_rep.edit()
            elif self.model.status == 2:
                stock_rep = repository.new_stock_repository(self.model)
                return stock_rep.remove()
            else:
                return Exception("Error: status invalido.")
        else:
            return Exception("Error: Estoque já sincronizado.")

    def local(self):
        self.backup_db()
        stock_rep = repository.new_stock_repository(self.model)
        stock_rep.backup("internal/backup/backupDB_stock_dump.sql")
        try:
            with open("internal/backup/backupDB_stock_dump.sql", 'r') as arquivo_sql:
                conteudo_sql = arquivo_sql.read()
            return conteudo_sql
        except Exception as error:
            return error
