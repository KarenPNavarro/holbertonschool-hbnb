"""Defines the BaseModel parent class for all entities."""
import uuid
from datetime import datetime


class BaseModel:
    """Base class providing id, timestamps, and shared methods."""

    def __init__(self):
        """Initialize id and creation/update timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp when the object changes."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Apply a dictionary of changes, then save."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
