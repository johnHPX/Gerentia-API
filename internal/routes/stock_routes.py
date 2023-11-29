from flask import Flask, request, jsonify
import internal.model as model
import internal.controller as controller


def init_stock_routes(app: Flask):
    # Routes stock
    @app.route('/api/stock/sinc', methods=['POST', 'PUT', 'DELETE'])
    def synchronize_to_api_stock():
        obj = request.get_json()

        if obj['status'] == 2:
            stock_model = model.Estoque(
                cod=obj['cod'], status=obj['status'], sincronizado=obj['sincronizado'])
        else:
            stock_model = model.Estoque(
                obj['cod'], obj['nome'], obj['descricao'], obj['quantidade'], obj['preco_compra'],
                obj['preco_venda'], obj['data_atual'], obj['hora_atual'], obj['status'], obj['sincronizado']
            )

        stock_controller = controller.new_stock_controller(stock_model)
        error = stock_controller.synchronize()

        if error != None:
            response = jsonify({"error": error.args[0]})
            response.status_code = 500
            app.logger.info('GET /api/admin/local HTTP/1.1 500')
            return response

        response = jsonify({"MID": "OK!"})
        response.status_code = 200
        app.logger.info('GET /api/admin/local HTTP/1.1 200')
        return response

    @app.route('/api/stock/local', methods=['GET'])
    def synchronize_to_local_stock():
        stock_model = model.Estoque()
        stock_controller = controller.new_stock_controller(stock_model)
        result = stock_controller.local()

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
