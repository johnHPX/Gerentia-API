from flask import request, jsonify


def init_sales_routes(app):
    # Routes sales
    @app.route('/api/sales/sinc', methods=['POST'])
    def synchronize_sales():
        obj = request.get_json()
        return jsonify({"MID": "Ok!"})

    @app.route('/api/sales/local', methods=['GET'])
    def local_sales():
        return jsonify({"MID": "Ok!"})
