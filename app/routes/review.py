from flask import Blueprint,jsonify,request,make_response
from app.models import Review

review_bp=Blueprint("review",__name__)
@review_bp.route('/all')
def reviews():
    reviews=[]
    for review in Review.query.all():
        review_dict=review.to_dict(rules=("-game","-user"))
        reviews.append(review_dict)
    response=make_response(
        reviews,
        200
    )
    return response
