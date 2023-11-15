import internal.controller.stock_controller as stock_controller


def new_stock_controller(estoque_model):
    return stock_controller.Estoque_Controller(estoque_model)
