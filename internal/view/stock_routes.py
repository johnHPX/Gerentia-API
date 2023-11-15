from flask import request, jsonify
import internal.model as model
import internal.controller as controller


def init_stock_routes(app):
    # Routes stock
    @app.route('/api/stock/sinc', methods=['POST'])
    def synchronize_stock():
        obj = request.get_json()

        # if isinstance(obj['hora_atual'], str):
        #     obj['hora_atual'] = datetime.strptime(
        #         obj['hora_atual'], '%H:%M:%S').time()

        stock_model = model.Estoque(
            obj['cod'], obj['nome'], obj['descricao'], obj['quantidade'], obj['preco_compra'],
            obj['preco_venda'], obj['data_atual'], obj['hora_atual'], obj['status'], obj['sincronizado']
        )

        stock_controller = controller.new_stock_controller(stock_model)
        stock_controller.synchronize()
        return jsonify({"MID": "Ok!"})

    @app.route('/api/stock/local', methods=['GET'])
    def local_stock():
        return jsonify({"MID": "Ok!"})
