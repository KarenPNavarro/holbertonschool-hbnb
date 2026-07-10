"""Defines the Place class."""
from app.models.base_model import BaseModel
from app.extensions import db


class Place(BaseModel):
    """Represents a property listed by a user."""

    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, title, description, price,
                 latitude, longitude):
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
