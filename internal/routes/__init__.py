from flask import Flask
# import internal.routes.admin_routes as admin_routes
import internal.routes.sales_routes as sales_routes
import internal.routes.stock_routes as stock_routes


def init_routes(app: Flask):
    # admin_routes.init_admin_routes(app)
    sales_routes.init_sales_routes(app)
    stock_routes.init_stock_routes(app)
