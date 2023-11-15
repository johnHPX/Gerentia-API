import internal.repository.stock_repository as stock_repository
import internal.repository.db_repository as db_repository


def new_stock_repository(estoque_model):
    return stock_repository.Estoque_Repository(estoque_model)


def new_db_repository():
    return db_repository.Database_Repository()
