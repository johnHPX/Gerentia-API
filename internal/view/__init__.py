from flask import Flask
from internal.view.templates_routes import init_templates_routes


def init_view(app: Flask):
    init_templates_routes(app)
