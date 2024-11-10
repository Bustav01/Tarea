from flask import Flask
from .routes import app_routes

def create_app():
    '''Inicialización de aplicación'''
    app = Flask(__name__,template_folder='templates')
    #importar rutas
    from .routes import app_routes
    app.register_blueprint(app_routes)
    return app

