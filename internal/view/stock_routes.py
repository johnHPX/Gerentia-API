from flask import Flask, request, jsonify, abort
import internal.model as model
import internal.controller as controller


def init_stock_routes(app: Flask):
    # Routes stock
    @app.route('/api/stock/sinc', methods=['POST', 'PUT', 'DELETE'])
    def synchronize_to_api_stock():
        obj = request.get_json()

        stock_model = model.Estoque(
            obj['cod'], obj['nome'], obj['descricao'], obj['quantidade'], obj['preco_compra'],
            obj['preco_venda'], obj['data_atual'], obj['hora_atual'], obj['status'], obj['sincronizado']
        )

        stock_controller = controller.new_stock_controller(stock_model)
        error = stock_controller.synchronize()

        if error != None:
            response = jsonify({"error": error.args[0]})
            response.status_code = 500
            return response

        response = jsonify({"MID": "OK!"})
        response.status_code = 200
        return response

    @app.route('/api/stock/local', methods=['GET'])
    def synchronize_to_local_stock():
        return jsonify({"MID": "Ok!"})
