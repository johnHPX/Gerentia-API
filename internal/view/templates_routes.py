from flask import Flask, render_template


def init_templates_routes(app: Flask):
    # Routes templates
    @app.route('/',  methods=['GET'])
    @app.route('/home', methods=['GET'])
    def home():
        return render_template("home.html")
