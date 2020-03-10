from flask_restplus import Api
from flask import Blueprint

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint,
          title='Test',
          version='1.0',
          description='API web service'
          )