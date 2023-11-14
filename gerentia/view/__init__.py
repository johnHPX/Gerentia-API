from flask import render_template, request, jsonify
from gerentia.controller import synchronize_db

def init_app_view(app):

    @app.route('/')
    @app.route('/home')
    def home():
        return render_template("home.html")
    
    # @app.route('/api/estoque/db/sinc', methods=['GET', 'POST'])
    # def sincronizar():
    #     content = request.get_json()
    #     return jsonify({"OK": "Okay!"})
    
    @app.route('/api/estoque/sinc')
    def synchronize():
        schemas = synchronize_db()
        return schemas
    
    @app.route('/api/estoque/up', methods=['GET', 'POST'])
    def update():
        content = request.get_json()
        return jsonify({"OK": "Okay!"})

    