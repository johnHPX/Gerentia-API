from flask import Flask, request, jsonify, make_response
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
            resp = make_response(jsonify({"MID": error}))
            resp.status_code = 500
            return resp

        resp = make_response(jsonify({"MID": "Ok!"}))
        resp.status_code = 200
        return resp

    @app.route('/api/stock/local', methods=['GET'])
    def synchronize_to_local_stock():
        return jsonify({"MID": "Ok!"})
