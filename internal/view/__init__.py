from flask import render_template, request, jsonify
import internal.controller as controller


def init_view(app):

    @app.route('/')
    @app.route('/home')
    def home():
        return render_template("home.html")

    @app.route('/api/stock/sinc', methods=['POST'])
    def synchronize():
        obj = request.get_json()
        controller.synchronize_db(obj)
        return jsonify({"MID": "Ok!"})
