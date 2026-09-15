from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from sqlalchemy import DeclarativeBase

class Base(DeclarativeBase):
    pass
db=SQLAlchemy(model_class=Base)
migrate-Migrate()
