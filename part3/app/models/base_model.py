"""Defines the BaseModel parent class for all entities."""
import uuid
from datetime import datetime
from app.extensions import db


class BaseModel(db.Model):
    """Base class providing id, timestamps, and shared methods."""

    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now,
                           onupdate=datetime.now)

    def save(self):
        """Update the updated_at timestamp and commit."""
        self.updated_at = datetime.now()
        db.session.commit()

    def update(self, data):
        """Apply a dictionary of changes, then save."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
