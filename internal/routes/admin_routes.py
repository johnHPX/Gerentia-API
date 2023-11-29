from flask import Flask, request, jsonify
import internal.model as model
import internal.controller as controller


def init_admin_routes(app: Flask):
    # Routes admin
    @app.route('/api/admin/sinc', methods=['POST'])
    def synchronize_to_api_admin():
        obj = request.get_json()

        if obj['status'] == 2:
            admin_model = model.Funcionarios(
                matricula=obj['matricula'], status=obj['status'], sincronizado=obj['sincronizado'])
        else:
            admin_model = model.Funcionarios(
                obj['matricula'], obj['nome'], obj['cargo'], obj['nome_usuario'], obj['senha'], obj['data_atual'], obj['hora_atual'], obj['status'], obj['sincronizado'])

        admin_controller = controller.new_admin_controller(admin_model)
        error = admin_controller.synchronize()

        if error != None:
            response = jsonify({"error": error.args[0]})
            response.status_code = 500
            return response

        response = jsonify({"MID": "OK!"})
        response.status_code = 200
        return response

    @app.route('/api/admin/local', methods=['GET'])
    def synchronize_to_local_admin():
        admin_model = model.Funcionarios()
        admin_controller = controller.new_admin_controller(admin_model)
        result = admin_controller.local()

        if result is Exception:
            response = jsonify({"error": result.args[0]})
            response.status_code = 500
            return response

        resp_obj = {
            "Content": result,
            "MID": "OK!"
        }

        response = jsonify(resp_obj)
        response.status_code = 200
        return response
