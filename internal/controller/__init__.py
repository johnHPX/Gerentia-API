import internal.controller.stock_controller as stock_controller
from internal.model import Estoque


def new_stock_controller(estoque_model: Estoque):
    return stock_controller.Estoque_Controller(estoque_model)
