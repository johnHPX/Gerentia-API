from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
import json
import internal.routes as routes


def read_configs():
    # Reading config.json
    with open('config/config.json', 'r', encoding='utf-8') as arquivo:
        config = json.load(arquivo)
    return config


def main():
    config = read_configs()

    # Configuração básica do logger
    logging.basicConfig(level=logging.INFO)

    # Configuração para salvar logs em um arquivo
    log_handler = RotatingFileHandler(
        'internal/logs/gerentia.log', maxBytes=10240, backupCount=10)
    log_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    log_handler.setLevel(logging.INFO)

    app = Flask(
        config['Project_Name'],
        root_path=config['Root_Path']
    )

    # Adiciona o handler ao logger da aplicação
    app.logger.addHandler(log_handler)

    routes.init_routes(app)
    
    print(f'Version: {config["Version"]}')
    app.run(port=config["API_Port"], debug=config["Dev_mode"])


if __name__ == '__main__':
    main()
