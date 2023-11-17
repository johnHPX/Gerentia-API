from internal.model import Vendas
import internal.repository as repository


class Vendas_Controller:
    def __init__(self, vendas_model: Vendas) -> None:
        self.model = vendas_model

    def backup_db(self):
        db_rep = repository.new_db_repository()
        db_rep.backup_db()

    def synchronize(self):
        self.backup_db()
        if self.model.sincronizado == 0:
            if self.model.status == 0:
                sales_repository = repository.new_sales_repository(self.model)
                error = sales_repository.store()
                return error
            elif self.model.status == 1:
                sales_repository = repository.new_sales_repository(self.model)
                error = sales_repository.edit()
                return error
            elif self.model.status == 2:
                sales_repository = repository.new_sales_repository(self.model)
                error = sales_repository.remove()
                return error
            else:
                return Exception("Erro: Status não é valido.")
        else:
            return Exception("Erro: Registro já sincronizado.")

    def local(self):
        self.backup_db()
        sale_rep = repository.new_sales_repository(self.model)
        sale_rep.backup("internal/backup/backupDB_sales_dump.sql")
        try:
            with open("internal/backup/backupDB_sales_dump.sql", 'r') as arquivo_sql:
                conteudo_sql = arquivo_sql.read()
            return conteudo_sql
        except Exception as error:
            return error
