"""User API endpoints."""
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='Password')
})

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name')
})


def user_to_dict(user):
    """Build the response dict for a user (never the password)."""
    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }


@api.route('/')
class UserList(Resource):
    """Handles the user collection (create and list)."""

    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user (public)"""
        user_data = api.payload
        existing = facade.get_user_by_email(user_data['email'])
        if existing:
            return {'error': 'Email already registered'}, 400
        try:
            new_user = facade.create_user(user_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        return user_to_dict(new_user), 201

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Get the list of all users (public)"""
        users = facade.get_all_users()
        return [user_to_dict(u) for u in users], 200


@api.route('/<user_id>')
class UserResource(Resource):
    """Handles a single user (retrieve and update)."""

    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID (public)"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return user_to_dict(user), 200

    @api.expect(user_update_model, validate=True)
    @jwt_required()
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Cannot modify email or password')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Update your own profile (not email or password)"""
        current_user_id = get_jwt_identity()
        if user_id != current_user_id:
            return {'error': 'Unauthorized action'}, 403
        data = api.payload
        if 'email' in data or 'password' in data:
            return {'error': 'You cannot modify email or password'}, 400
        try:
            updated = facade.update_user(user_id, data)
        except ValueError as e:
            return {'error': str(e)}, 400
        if not updated:
            return {'error': 'User not found'}, 404
        return user_to_dict(updated), 200
