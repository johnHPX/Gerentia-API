from flask import Flask, request, jsonify
import internal.model as model
import internal.controller as controller


def init_stock_routes(app: Flask):
    # Routes stock
    @app.route("/api/stock/sinc", methods=["POST"])
    def synchronize_to_api_stock():
        obj = request.get_json()
        stock_model = model.Estoque()

        if obj["status"] == 2:
            stock_model.cod = obj["cod"]
            stock_model.status = obj["status"]
            stock_model.sincronizado = obj["sincronizado"]
        else:
            stock_model.cod = obj["cod"]
            stock_model.nome = obj["nome"]
            stock_model.descricao = obj["descricao"]
            stock_model.quantidade = obj["quantidade"]
            stock_model.preco_compra = obj["preco_compra"]
            stock_model.preco_venda = obj["preco_venda"]
            stock_model.data_atual = obj["data_atual"]
            stock_model.hora_atual = obj["hora_atual"]
            stock_model.status = obj["status"]
            stock_model.sincronizado = obj["sincronizado"]

        stock_controller = controller.new_stock_controller(stock_model)
        result = stock_controller.synchronize()

        if result != None:
            if result.args[0] > 200:
                body = {
                    "status": "error",
                    "message": result.args[1],
                    "cod": result.args[0],
                    "layer": "controller",
                }
                response = jsonify(body)
                response.status_code = 422
                app.logger.info("POST /api/stock/sinc HTTP/1.1 422")
                app.logger.info(f"COD: {result.args[0]}")
                app.logger.info(f"MESSAGE: {result.args[1]}")
                app.logger.info("LAYER: controller")
                return response
            else:
                body = {
                    "status": "error",
                    "message": result.args[1],
                    "cod": result.args[0],
                    "layer": "repository",
                }
                response = jsonify(body)
                response.status_code = 500
                app.logger.info("POST /api/stock/sinc HTTP/1.1 500")
                app.logger.info(f"COD: {result.args[0]}")
                app.logger.info(f"MESSAGE: {result.args[1]}")
                app.logger.info("LAYER: repository")
                return response

        response = jsonify({"MID": "OK!"})
        response.status_code = 200
        app.logger.info("POST /api/stock/sinc HTTP/1.1 200")
        app.logger.info("MID: OK!")
        return response

    @app.route("/api/stock/local", methods=["GET"])
    def synchronize_to_local_stock():
        stock_model = model.Estoque()
        stock_controller = controller.new_stock_controller(stock_model)
        result = stock_controller.local()

        if result is Exception:
            response = jsonify({"error": result.args[0]})
            response.status_code = 500
            app.logger.info("GET /api/stock/local HTTP/1.1 500")
            return response

        resp_obj = {"Content": result, "MID": "OK!"}

        response = jsonify(resp_obj)
        response.status_code = 200
        app.logger.info("GET /api/stock/local HTTP/1.1 200")
        return response
