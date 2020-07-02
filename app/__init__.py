from flask import Flask
from flask_cors import CORS


def create_app(config_class=None):
    app = Flask(__name__)
    # if __name__ == '__main__':
    #     app.run(host='0.0.0.0', port=8081)
    CORS(app)
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    # print(app.url_map)
    return app
