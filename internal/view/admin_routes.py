from flask import request, jsonify


def init_admin_routes(app):
    # Routes admin
    @app.route('/api/admin/sinc', methods=['POST'])
    def synchronize_admin():
        obj = request.get_json()
        return jsonify({"MID": "Ok!"})

    @app.route('/api/admin/local', methods=['GET'])
    def local_admin():
        return jsonify({"MID": "Ok!"})
