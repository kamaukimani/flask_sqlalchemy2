from flask import Flask 
from .db import db,migrate
from .config import Config
from .models import *
from .routes import game_bp,user_bp
 

def create_app():
    app=Flask(__name__)

    app.config.from_object(Config)
    app.json.compact=False

    db.init_app(app)
    migrate.init_app(app,db)

    
    app.register_blueprint(game_bp,url_prefix="/game")
    app.register_blueprint(user_bp,url_prefix="/user")
    
    return app

