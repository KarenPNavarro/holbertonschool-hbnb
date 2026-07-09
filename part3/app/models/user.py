"""Defines the User class."""
import re
from app.models.base_model import BaseModel


class User(BaseModel):
    """Represents a person using the application."""

    def __init__(self, first_name, last_name, email, is_admin=False):
        """Initialize a user with validated attributes."""
        super().__init__()
        if not first_name or len(first_name) > 50:
            raise ValueError("first_name is required (max 50 chars)")
        if not last_name or len(last_name) > 50:
            raise ValueError("last_name is required (max 50 chars)")
        if not self.is_valid_email(email):
            raise ValueError("a valid email is required")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    @staticmethod
    def is_valid_email(email):
        """Return True if the email has a valid basic format."""
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        return bool(email) and re.match(pattern, email) is not None
