from flask import Flask 
from .db import db,migrate
from .config import Config
from .models import *
 

def create_app():
    app=Flask(__name__)

    app.config.from_object(Config)
    app.json.compact=False

    db.init_app(app)
    migrate.init_app(app,db)

    

    
    return app

