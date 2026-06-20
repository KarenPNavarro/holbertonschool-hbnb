"""Place API endpoints."""
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title'),
    'description': fields.String(description='Description'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude'),
    'longitude': fields.Float(required=True, description='Longitude'),
    'owner_id': fields.String(required=True, description='Owner id'),
    'amenities': fields.List(fields.String, description='Amenity ids')
})


def place_to_dict(place):
    """Build the full response for a place, with nested data."""
    return {
        'id': place.id,
        'title': place.title,
        'description': place.description,
        'price': place.price,
        'latitude': place.latitude,
        'longitude': place.longitude,
        'owner': {
            'id': place.owner.id,
            'first_name': place.owner.first_name,
            'last_name': place.owner.last_name,
            'email': place.owner.email
        },
        'amenities': [{'id': a.id, 'name': a.name}
                      for a in place.amenities]
    }


@api.route('/')
class PlaceList(Resource):
    """Handles the place collection (create and list)."""

    @api.expect(place_model, validate=True)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload
        try:
            new_place = facade.create_place(place_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        return place_to_dict(new_place), 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Get the list of all places"""
        places = facade.get_all_places()
        return [place_to_dict(p) for p in places], 200


@api.route('/<place_id>')
class PlaceResource(Resource):
    """Handles a single place (retrieve and update)."""

    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return place_to_dict(place), 200

    @api.expect(place_model, validate=True)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        try:
            updated = facade.update_place(place_id, place_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        if not updated:
            return {'error': 'Place not found'}, 404
        return place_to_dict(updated), 200
