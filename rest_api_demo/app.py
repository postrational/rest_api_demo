import logging.config

from flask import Flask, Blueprint
from rest_api_demo.api.blog.endpoints import ns as blog_namespace
from rest_api_demo.api.restplus import api

app = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = 'localhost:8888'
    flask_app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
    flask_app.config.RESTPLUS_VALIDATE = True


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(blog_namespace)
    flask_app.register_blueprint(blueprint)


def main():
    initialize_app(app)
    print('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=True)

if __name__ == "__main__":
    main()
