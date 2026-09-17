from flask import Blueprint,jsonify,request,make_response
from app.models import Review
from app.db import db

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

@review_bp.route('/<int:id>',methods=["GET","DELETE","PATCH"])
def review_by_id(id):
    review=Review.query.filter_by(id=id).first()

    if review is None:
        response_body={
            "message":"This record does not  exist in our database!!!!"
        }
        return make_response(response_body,404)
    if request.method == "GET":
        review_dict=review.to_dict(rules=("-game","-user"))
        response=make_response(
            review_dict,
            200
        )
        return response 
    elif request.method == "DELETE":
        db.session.delete(review)
        db.session.commit()

        response_body={
            "deleted_successfull":True,
            "message":"Review deleted successfully"
        }
        response=make_response(
            response_body,
            200
        )
        return response
    elif request.method == "PATCH":
        data=request.get_json()

        for attr in data:
            setattr(review,attr,data[attr])

        db.session.add(review)
        db.session.commit()

        review_dict=review.to_dict(rules=("-game","-user"))
        
        response=make_response(
            review_dict,
            200
        )
        return response

@review_bp.route('/reviews',methods=["GET","POST"])
def revieews():
    if request.method == "GET":
        reviews=[]
        for review in Review.query.all():
            review_dict=review.to_dict(rules=("-game","-user"))
            reviews.append(review_dict)
        response=make_response(
            reviews,
            200
        )
        return response
    elif request.method == "POST":
        data=request.get_json()
        score=data["score"]
        comment=data["comment"]
        game_id=data.get("game_id")
        user_id=data.get("user_id")
        new_review=Review(
            score=score,
            comment=comment,
            game_id=game_id,
            user_id=user_id,
        )
        db.session.add(new_review)
        db.session.commit()

        review_dict=new_review.to_dict()

        response=make_response(
            review_dict,
            201
        )
        return response

    