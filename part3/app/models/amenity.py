"""Defines the Amenity class."""
from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a feature a place can offer (e.g. wifi)."""

    def __init__(self, name):
        """Initialize an amenity with a validated name."""
        super().__init__()
        if not name or len(name) > 50:
            raise ValueError("name is required (max 50 chars)")
        self.name = name
