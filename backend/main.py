from flask import Flask, jsonify


def create_app(config_object=None):
    app = Flask(__name__,
                static_folder="./webapp/dist/static",
                template_folder="./webapp/dist")

    app.config.from_object(config_object)

    @app.route('/')
    def api():
        return 'Hello World'

    return app
