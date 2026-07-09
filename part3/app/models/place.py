"""Defines the Place class."""
from app.models.base_model import BaseModel


class Place(BaseModel):
    """Represents a property listed by a user."""

    def __init__(
        self, title, description, price,
        latitude, longitude, owner
    ):
        """Initialize a place with validated attributes."""
        super().__init__()
        if not title or len(title) > 100:
            raise ValueError("title is required (max 100 chars)")
        if price <= 0:
            raise ValueError("price must be a positive number")
        if not -90 <= latitude <= 90:
            raise ValueError("latitude must be between -90 and 90")
        if not -180 <= longitude <= 180:
            raise ValueError("longitude must be between -180 and 180")
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """Add a review to this place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to this place."""
        self.amenities.append(amenity)
