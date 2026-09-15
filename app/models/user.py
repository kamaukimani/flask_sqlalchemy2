from datetime import datetime
from sqlalchemy import func,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.db import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


class User(db.Model,SerializerMixin):
    __tablename__="users"

    serialize_rules=("-reviews.user",)

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(unique=True)
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(server_default=func.now(),onupdate=func.now())

    reviews:Mapped[List["Review"]]=relationship(back_populates="user",cascade="all,delete-orphan")

    games=association_proxy("reviews","game",creator=lambda game_obj:Review(game=game_obj))

    def __repr__(self):
        return f"<User ({seld.id}) {self.name}>"
