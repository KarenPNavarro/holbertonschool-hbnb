"""Defines the Place class."""
from app.models.base_model import BaseModel
from app.extensions import db


place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.String(36),
              db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(36),
              db.ForeignKey('amenities.id'), primary_key=True)
)


class Place(BaseModel):
    """Represents a property listed by a user."""

    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'),
                         nullable=False)

    reviews = db.relationship('Review', backref='place',
                              lazy=True, cascade='all, delete-orphan')
    amenities = db.relationship('Amenity', secondary=place_amenity,
                                backref='places', lazy='subquery')

    def __init__(self, title, description, price,
                 latitude, longitude, owner):
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

    def add_amenity(self, amenity):
        """Link an amenity to this place."""
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def add_review(self, review):
        """Link a review to this place."""
        self.reviews.append(review)
