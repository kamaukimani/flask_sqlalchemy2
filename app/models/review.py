from datetime import datetime
from sqlalchemy import func,ForeignKey
from sqlalchemy.orm import Mapped,mappped_column,relationship
from app.db import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

class Review(db.Model,SerializerMixin):
    __tablename__="reviews"

    id:Mapped[int]=mapped_column(primary_key=True)
    score:Mapped[int]
    comment:Mapped[str]
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(server_default=func.now(),onupdate=func.now())
    
    game_id:Mapped[int]=mapped_column(ForeignKey("games.id"))
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"))