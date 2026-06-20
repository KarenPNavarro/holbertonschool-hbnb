"""Review API endpoints."""
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating (1-5)'),
    'user_id': fields.String(required=True, description='User id'),
    'place_id': fields.String(required=True, description='Place id')
})


def review_to_dict(review):
    """Build the response dict for a review."""
    return {
        'id': review.id,
        'text': review.text,
        'rating': review.rating,
        'user_id': review.user.id,
        'place_id': review.place.id
    }


@api.route('/')
class ReviewList(Resource):
    """Handles the review collection (create and list)."""

    @api.expect(review_model, validate=True)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        review_data = api.payload
        try:
            new_review = facade.create_review(review_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        return review_to_dict(new_review), 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Get the list of all reviews"""
        reviews = facade.get_all_reviews()
        return [review_to_dict(r) for r in reviews], 200


@api.route('/<review_id>')
class ReviewResource(Resource):
    """Handles a single review (retrieve, update, delete)."""

    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return review_to_dict(review), 200

    @api.expect(review_model, validate=True)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    def put(self, review_id):
        """Update a review's information"""
        review_data = api.payload
        updated = facade.update_review(review_id, review_data)
        if not updated:
            return {'error': 'Review not found'}, 404
        return review_to_dict(updated), 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        if not facade.delete_review(review_id):
            return {'error': 'Review not found'}, 404
        return {'message': 'Review deleted successfully'}, 200
