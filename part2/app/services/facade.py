"""Facade coordinating the application's layers."""
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity


class HBnBFacade:
    """Single entry point between the API and the business logic."""

    def __init__(self):
        """Initialize one repository per entity type."""
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        """Create and store a new user."""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Return a user by id, or None."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Return a user matching the email, or None."""
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        """Return every stored user."""
        return self.user_repo.get_all()

    def update_user(self, user_id, data):
        """Update an existing user and return it, or None."""
        user = self.user_repo.get(user_id)
        if not user:
            return None
        user.update(data)
        return user

    def create_amenity(self, amenity_data):
        """Create and store a new amenity."""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Return an amenity by id, or None."""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Return every stored amenity."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, data):
        """Update an existing amenity and return it, or None."""
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        amenity.update(data)
        return amenity
