from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped,mappped_column,relationship
from app.db import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

class Game(db.Model,SerializerMixin):
    __tablename__="games"

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]
    genre:Mapped[str]
    platform:Mapped[str]
    price:Mapped[int]
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(server_default=func.now(),onupdate=func.now())

    reviews:Mapped[List["Review"]]=relationship(back_populates="game", cascade="all,delete-orphan")

    users=association_proxy("reviews","user",creator=lambda user_obj:Review(user=user_obj))
