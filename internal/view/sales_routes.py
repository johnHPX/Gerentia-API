from flask import Flask, request, jsonify
import internal.model as model
import internal.controller as controller


def init_sales_routes(app: Flask):
    # Routes sales
    @app.route('/api/sales/sinc', methods=['POST', 'PUT', 'DELETE'])
    def synchronize_to_api_sales():
        obj = request.get_json()
        sales_model = model.Vendas(
            obj['id'], obj['nome'], obj['quantidade'], obj['valor'],
            obj['total'], obj['data'], obj['hora'], obj['status'], obj['sincronizado']
        )

        sales_controller = controller.new_sales_controller(sales_model)
        error = sales_controller.synchronize()

        if error != None:
            response = jsonify({"error": error.args[0]})
            response.status_code = 500
            return response

        response = jsonify({"MID": "OK!"})
        response.status_code = 200
        return response

    @app.route('/api/sales/local', methods=['GET'])
    def synchronize_to_local_sales():
        sales_model = model.Vendas()
        sales_controller = controller.new_sales_controller(sales_model)
        result = sales_controller.local()

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
