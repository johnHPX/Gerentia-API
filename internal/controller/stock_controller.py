import internal.repository as repository
from internal.model import Estoque


class Estoque_Controller:
    def __init__(self, estoque_model: Estoque) -> None:
        self.model = estoque_model

    def backup_db(self):
        stock_rep = repository.new_stock_repository(self.model)
        stock_rep.backup("internal/backup/backupDB_stock_dump.sql")
        
    def synchronize(self):
        self.backup_db()
        stock_rep = repository.new_stock_repository(self.model)
        stock_rep.start_conection()
        if self.model.sincronizado == 0:
            if self.model.status == 0:
                result = stock_rep.store()
                stock_rep.close_connection()
                return result
            
            elif self.model.status == 1:
                result_exists = stock_rep.verific_stock_exists()
                if result_exists == True:
                    result = stock_rep.edit()
                    stock_rep.close_connection()
                    return result
                
                result_store = stock_rep.store()
                if result_store is None:
                    result_edit = stock_rep.edit()
                    stock_rep.close_connection()
                    return result_edit
                
                return result_store
                
            elif self.model.status == 2:
                result_exists = stock_rep.verific_stock_exists()
                if result_exists == True:
                    result_remove = stock_rep.remove()
                    stock_rep.close_connection()
    
                    return result_remove              

                result_store = stock_rep.store()
                if result_store is None:
                    result_remove = stock_rep.remove()
                    stock_rep.close_connection()
                    return result_remove   
                
                return result_store
            else:
                return Exception(201, "Erro: Status não é valido.")
        else:
            return Exception(202, "Erro: Registro já sincronizado.")
        

    def local(self):
        self.backup_db()
        stock_rep = repository.new_stock_repository(self.model)
        return stock_rep.list()
