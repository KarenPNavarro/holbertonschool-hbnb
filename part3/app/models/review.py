"""Defines the Review class."""
from app.models.base_model import BaseModel
from app.extensions import db


class Review(BaseModel):
    """Represents a review left by a user on a place."""

    __tablename__ = 'reviews'

    text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'),
                        nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'),
                         nullable=False)

    def __init__(self, text, rating, user, place):
        """Initialize a review with validated attributes."""
        super().__init__()
        if not text:
            raise ValueError("text is required")
        if not 1 <= rating <= 5:
            raise ValueError("rating must be between 1 and 5")
        self.text = text
        self.rating = rating
        self.user = user
        self.place = place
