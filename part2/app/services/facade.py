"""Facade coordinating the application's layers."""
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place


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

    def create_place(self, place_data):
        """Create a place, resolving its owner and amenities."""
        owner = self.user_repo.get(place_data.get('owner_id'))
        if not owner:
            raise ValueError("Owner not found")
        place = Place(
            title=place_data['title'],
            description=place_data.get('description', ''),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner=owner
        )
        for amenity_id in place_data.get('amenities', []):
            amenity = self.amenity_repo.get(amenity_id)
            if amenity:
                place.add_amenity(amenity)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Return a place by id, or None."""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Return every stored place."""
        return self.place_repo.get_all()

    def update_place(self, place_id, data):
        """Update a place, re-resolving owner and amenities."""
        place = self.place_repo.get(place_id)
        if not place:
            return None
        if 'owner_id' in data:
            owner = self.user_repo.get(data['owner_id'])
            if not owner:
                raise ValueError("Owner not found")
            place.owner = owner
        if 'amenities' in data:
            place.amenities = []
            for amenity_id in data['amenities']:
                amenity = self.amenity_repo.get(amenity_id)
                if amenity:
                    place.add_amenity(amenity)
        simple = {k: v for k, v in data.items()
                if k not in ('owner_id', 'amenities')}
        place.update(simple)
        return place
