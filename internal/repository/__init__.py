import internal.repository.stock_repository as stock_repository
import internal.repository.sales_repository as sales_repository
import internal.repository.db_repository as db_repository
from internal.model import Estoque, Vendas


def new_stock_repository(estoque_model: Estoque):
    return stock_repository.Estoque_Repository(estoque_model)


def new_sales_repository(vendas_model: Vendas):
    return sales_repository.Vendas_Repository(vendas_model)


def new_db_repository():
    return db_repository.Database_Repository()
