import internal.controller.stock_controller as stock_controller
import internal.controller.sales_contoller as sales_controller
from internal.model import Estoque, Vendas


def new_stock_controller(estoque_model: Estoque):
    return stock_controller.Estoque_Controller(estoque_model)


def new_sales_controller(vendas_model: Vendas):
    return sales_controller.Vendas_Controller(vendas_model)
