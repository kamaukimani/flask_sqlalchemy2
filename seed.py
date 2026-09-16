#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import create_app,db
from app.models import Game, Review, User


fake = Faker()
app=create_app()
with app.app_context():

    Review.query.delete()
    User.query.delete()
    Game.query.delete()

    users = []
    for i in range(3):
        u = User(name=fake.name())
        users.append(u)

    db.session.add_all(users)

    games = []
    games.append(Game(
        title='Mega Adventure',
        genre='Survival',
        platform='XBox',
        price=30))
    games.append(Game(
        title='Golf Pro IV',
        genre='Sports',
        platform="PlayStation",
        price=20))
    games.append(Game(
        title='Dance, dance, dance',
        genre='Party',
        platform="PlayStation",
        price=7))
    db.session.add_all(games)

    reviews = []
    reviews.append(Review(
        score=9,
        comment='Amazing action',
        user=users[0],
        game=games[0]))
    reviews.append(Review(
        score=2,
        comment='Boring',
        user=users[0],
        game=games[1]))
    reviews.append(Review(
        score=5,
        comment='Not enough levels',
        user=users[1],
        game=games[0]))
    reviews.append(Review(
        score=randint(0, 10),
        comment='confusing instructions',
        user=users[2],
        game=games[2]))
    db.session.add_all(reviews)

   

    db.session.commit()