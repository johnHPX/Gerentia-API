from flask import Flask, request, jsonify


def init_sales_routes(app: Flask):
    # Routes sales
    @app.route('/api/sales/sinc', methods=['POST'])
    def synchronize_to_api_sales():
        obj = request.get_json()
        return jsonify({"MID": "Ok!"})

    @app.route('/api/sales/local', methods=['GET'])
    def synchronize_to_local_sales():
        return jsonify({"MID": "Ok!"})
