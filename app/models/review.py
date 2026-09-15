from datetime import datetime
from sqlalchemy import func,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.db import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from typing import List

class Review(db.Model,SerializerMixin):
    __tablename__="reviews"

    serialize_rules=("-game.reviews","-user.reviews",)

    id:Mapped[int]=mapped_column(primary_key=True)
    score:Mapped[int]
    comment:Mapped[str]
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(server_default=func.now(),onupdate=func.now())
    
    game_id:Mapped[int]=mapped_column(ForeignKey("games.id"),primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),primary_key=True)

    game:Mapped["Game"]=relationship(back_populates="reviews")
    user:Mapped["User"]=relationship(back_populates="reviews")

    def __repr__(self):
        return f"<Review ({self.id}) of {self.game}: {self.score}/10>"