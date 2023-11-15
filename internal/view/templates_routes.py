from flask import render_template


def init_templates_routes(app):
    # Routes templates
    @app.route('/',  methods=['GET'])
    @app.route('/home', methods=['GET'])
    def home():
        return render_template("home.html")
