from flask import Blueprint,jsonify,request,make_response
from app.models import Game

game_bp=Blueprint("game",__name__)
@game_bp.route('/all')
def games():
    # games=[]
    # for game in Game.query.all():
    #     game_dict=game.to_dict()
    #     games.append(game_dict)

    games=[game.to_dict() for game in Game.query.all()]
    response=make_response(
        games,
        200
    )
    return response

@game_bp.route('/<int:id>')
def game_by_id(id):
    game=Game.query.filter(Game.id == id).first()
    game_dict=game.to_dict()
    
    response=make_response(
        game_dict,
        200
    )
    return response
@game_bp.route('/users/<int:id>')
def game_users_by_id(id):
    game=Game.query.filter_by(id=id).first()
    users=[]
    for user in game.users:
        user_dict=user.to_dict(rules=("-reviews",))
        users.append(user_dict)
    response=make_response(
        users,
        200
    )
    return users
