from flask import Blueprint,jsonify,request,make_response
from app.models import User

user_bp=Blueprint("user",__name__)
@user_bp.route('/all')
def users():
    users=[]
    for user in User.query.all():
        user_dict=user.to_dict(rules=("-reviews",))
        users.append(user_dict)
    response=make_response(
        users,
        200
    )
    return response