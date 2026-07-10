"""Review API endpoints."""
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating (1-5)')
})


def review_to_dict(review):
    """Build the response dict for a review (no relationships yet)."""
    return {
        'id': review.id,
        'text': review.text,
        'rating': review.rating
    }


@api.route('/')
class ReviewList(Resource):
    """Handles the review collection (create and list)."""

    @api.expect(review_model, validate=True)
    @jwt_required()
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        try:
            new_review = facade.create_review(api.payload)
        except ValueError as e:
            return {'error': str(e)}, 400
        return review_to_dict(new_review), 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Get the list of all reviews (public)"""
        reviews = facade.get_all_reviews()
        return [review_to_dict(r) for r in reviews], 200


@api.route('/<review_id>')
class ReviewResource(Resource):
    """Handles a single review (retrieve, update, delete)."""

    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID (public)"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return review_to_dict(review), 200

    @api.expect(review_model, validate=True)
    @jwt_required()
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    def put(self, review_id):
        """Update a review"""
        updated = facade.update_review(review_id, api.payload)
        if not updated:
            return {'error': 'Review not found'}, 404
        return review_to_dict(updated), 200

    @jwt_required()
    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        if not facade.delete_review(review_id):
            return {'error': 'Review not found'}, 404
        return {'message': 'Review deleted successfully'}, 200
