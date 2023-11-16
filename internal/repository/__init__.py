import internal.repository.stock_repository as stock_repository
import internal.repository.db_repository as db_repository
from internal.model import Estoque


def new_stock_repository(estoque_model: Estoque):
    return stock_repository.Estoque_Repository(estoque_model)


def new_db_repository():
    return db_repository.Database_Repository()
