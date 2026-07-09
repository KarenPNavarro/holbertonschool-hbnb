"""Unit tests for the HBnB API endpoints."""
import unittest
from app import create_app


class TestHBnBEndpoints(unittest.TestCase):
    """Test the API endpoints using Flask's test client."""

    def setUp(self):
        """Run before each test: build a fresh client."""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user_valid(self):
        """A valid user returns 201."""
        response = self.client.post('/api/v1/users/', json={
            'first_name': 'Karen',
            'last_name': 'Navarro',
            'email': 'karen@test.com'
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_email(self):
        """An invalid email returns 400."""
        response = self.client.post('/api/v1/users/', json={
            'first_name': 'Karen',
            'last_name': 'Navarro',
            'email': 'not-an-email'
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_empty_name(self):
        """An empty first name returns 400."""
        response = self.client.post('/api/v1/users/', json={
            'first_name': '',
            'last_name': 'Navarro',
            'email': 'karen2@test.com'
        })
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
