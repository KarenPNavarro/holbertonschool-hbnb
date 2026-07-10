"""Facade coordinating the application's layers."""
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository
from app.persistence.user_repository import UserRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    """Single entry point between the API and the business logic."""

    def __init__(self):
        """Initialize database-backed repositories for all entities."""
        self.user_repo = UserRepository()
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

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
        return self.user_repo.get_user_by_email(email)

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
        """Create and store a new place (no relationships yet)."""
        place = Place(
            title=place_data['title'],
            description=place_data.get('description', ''),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude']
        )
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Return a place by id, or None."""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Return every stored place."""
        return self.place_repo.get_all()

    def update_place(self, place_id, data):
        """Update a place and return it, or None."""
        place = self.place_repo.get(place_id)
        if not place:
            return None
        place.update(data)
        return place

    def create_review(self, review_data):
        """Create and store a new review (no relationships yet)."""
        review = Review(
            text=review_data['text'],
            rating=review_data['rating']
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        """Return a review by id, or None."""
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        """Return every stored review."""
        return self.review_repo.get_all()

    def update_review(self, review_id, data):
        """Update a review and return it, or None."""
        review = self.review_repo.get(review_id)
        if not review:
            return None
        review.update(data)
        return review

    def delete_review(self, review_id):
        """Delete a review. Return True if it existed."""
        review = self.review_repo.get(review_id)
        if not review:
            return False
        self.review_repo.delete(review_id)
        return True
