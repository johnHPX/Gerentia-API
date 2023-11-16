import internal.repository as repository
from internal.model import Estoque


class Estoque_Controller:
    def __init__(self, estoque_model: Estoque) -> None:
        self.model = estoque_model

    def synchronize(self):
        db_rep = repository.new_db_repository()
        db_rep.backup_db()
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
