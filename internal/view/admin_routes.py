from flask import Flask, request, jsonify


def init_admin_routes(app: Flask):
    # Routes admin
    @app.route('/api/admin/sinc', methods=['POST'])
    def synchronize_to_api_admin():
        obj = request.get_json()
        return jsonify({"MID": "Ok!"})

    @app.route('/api/admin/local', methods=['GET'])
    def synchronize_to_local_admin():
        return jsonify({"MID": "Ok!"})
