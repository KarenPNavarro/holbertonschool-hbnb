"""Defines the Amenity class."""
from app.models.base_model import BaseModel
from app.extensions import db


class Amenity(BaseModel):
    """Represents a feature a place can offer (e.g. wifi)."""

    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        """Initialize an amenity with a validated name."""
        super().__init__()
        if not name or len(name) > 50:
            raise ValueError("name is required (max 50 chars)")
        self.name = name
