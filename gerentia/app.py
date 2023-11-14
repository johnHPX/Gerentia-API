import gerentia.view as view 
from flask import Flask
import json

# Reading config.json
with open('config.json', 'r', encoding='utf-8') as arquivo:
    config = json.load(arquivo)

print(f'Verion: {config["Version"]}')
app = Flask(config['Project_Name'])
view.init_app_view(app)
