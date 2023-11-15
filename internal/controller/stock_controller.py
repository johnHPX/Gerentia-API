import internal.repository as repository


class Estoque_Controller:
    def __init__(self, estoque_model) -> None:
        self.model = estoque_model

    def synchronize(self):
        db_rep = repository.new_db_repository()
        db_rep.backup_db()
        if self.model.sincronizado == 0:
            if self.model.status == 0:
                stock_rep = repository.new_stock_repository(self.model)
                stock_rep.store()
            elif self.model.status == 1:
                pass
            elif self.model.status == 2:
                pass
