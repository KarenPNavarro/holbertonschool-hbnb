"""User-specific repository."""
from app.models.user import User
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    """Repository with user-specific database queries."""

    def __init__(self):
        """Bind this repository to the User model."""
        super().__init__(User)

    def get_user_by_email(self, email):
        """Return the user with this email, or None."""
        return self.model.query.filter_by(email=email).first()
