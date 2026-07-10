"""Place API endpoints."""
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title'),
    'description': fields.String(description='Description'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude'),
    'longitude': fields.Float(required=True, description='Longitude')
})


def place_to_dict(place):
    """Build the response for a place (no relationships yet)."""
    return {
        'id': place.id,
        'title': place.title,
        'description': place.description,
        'price': place.price,
        'latitude': place.latitude,
        'longitude': place.longitude
    }


@api.route('/')
class PlaceList(Resource):
    """Handles the place collection (create and list)."""

    @api.expect(place_model, validate=True)
    @jwt_required()
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        try:
            new_place = facade.create_place(api.payload)
        except ValueError as e:
            return {'error': str(e)}, 400
        return place_to_dict(new_place), 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Get the list of all places (public)"""
        places = facade.get_all_places()
        return [place_to_dict(p) for p in places], 200


@api.route('/<place_id>')
class PlaceResource(Resource):
    """Handles a single place (retrieve and update)."""

    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID (public)"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return place_to_dict(place), 200

    @api.expect(place_model, validate=True)
    @jwt_required()
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    def put(self, place_id):
        """Update a place"""
        try:
            updated = facade.update_place(place_id, api.payload)
        except ValueError as e:
            return {'error': str(e)}, 400
        if not updated:
            return {'error': 'Place not found'}, 404
        return place_to_dict(updated), 200
