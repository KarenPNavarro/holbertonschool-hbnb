"""Defines the User class."""
import re
from app.models.base_model import BaseModel
from app.extensions import db, bcrypt


class User(BaseModel):
    """Represents a person using the application."""

    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, email,
                 password=None, is_admin=False):
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
        if password:
            self.hash_password(password)

    @staticmethod
    def is_valid_email(email):
        """Return True if the email has a valid basic format."""
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        return bool(email) and re.match(pattern, email) is not None

    def hash_password(self, password):
        """Hash the password and store the hash."""
        self.password = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def verify_password(self, password):
        """Return True if the password matches the stored hash."""
        return bcrypt.check_password_hash(self.password, password)
