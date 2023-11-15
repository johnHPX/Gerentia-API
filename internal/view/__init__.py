from flask import request, jsonify
import internal.view.admin_routes as admin_routes
import internal.view.sales_routes as sales_routes
import internal.view.stock_routes as stock_routes
import internal.view.templates_routes as templates_routes


def init_view(app):
    admin_routes.init_admin_routes(app)
    sales_routes.init_sales_routes(app)
    stock_routes.init_stock_routes(app)
    templates_routes.init_templates_routes(app)
