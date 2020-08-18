from flask import Flask
from flask_cors import CORS
from app.api import bp as api_bp
from app.db import bp as db_bp


# Application factory
# https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/
def create_app(config_class=None):
    app = Flask(__name__)
    # if __name__ == '__main__':
    #     app.run(host='0.0.0.0', port=8081)
    CORS(app)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(db_bp, url_prefix='/db')
    # print(app.url_map)
    return app
