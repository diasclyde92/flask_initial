from flask_jwt_extended import (create_access_token, get_jwt_identity, JWTManager, jwt_required, get_raw_jwt)
from flask_script import Manager
from app import blueprint
from app.main import create_app
import os

app = create_app(os.getenv('FLASK_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()
jwt = JWTManager(app)
manager = Manager(app)
app.config['UPLOAD_FOLDER'] = "uploads/"
app.config['STATIC_FOLDER'] = "static/"

if __name__ == '__main__':
    app.run(debug=True)
    app.config['SOAP']=True