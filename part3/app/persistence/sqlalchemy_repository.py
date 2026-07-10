"""SQLAlchemy-based repository implementation."""
from app.extensions import db
from app.persistence.repository import Repository


class SQLAlchemyRepository(Repository):
    """A repository that persists objects using SQLAlchemy."""

    def __init__(self, model):
        """Store the model class this repository manages."""
        self.model = model

    def add(self, obj):
        """Insert an object and commit."""
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        """Return an object by its primary key, or None."""
        return self.model.query.get(obj_id)

    def get_all(self):
        """Return every stored object of this model."""
        return self.model.query.all()

    def update(self, obj_id, data):
        """Update an object's attributes and commit."""
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            db.session.commit()

    def delete(self, obj_id):
        """Delete an object and commit."""
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        """Return the first object matching an attribute, or None."""
        return self.model.query.filter_by(
            **{attr_name: attr_value}).first()
