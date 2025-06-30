import unittest
from app import app as flask_app
import json

class TestMamaCareApp(unittest.TestCase):
    def setUp(self):
        """Set up test client before each test."""
        self.app = flask_app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test that the home page loads successfully."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'MamaCare Assistant', response.data)

    def test_ask_endpoint(self):
        """Test the /ask endpoint with valid data."""
        test_data = {
            'question': 'What foods should I eat during pregnancy?',
            'trimester': '2nd',
            'diet': 'veg',
            'mood': 'happy'
        }
        
        response = self.app.post(
            '/ask',
            data=json.dumps(test_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('status', data)
        self.assertIn('response', data)

    def test_ask_endpoint_invalid_data(self):
        """Test the /ask endpoint with invalid data."""
        test_data = {
            'question': '',  # Empty question should be invalid
            'trimester': '2nd',
            'diet': 'veg',
            'mood': 'happy'
        }
        
        response = self.app.post(
            '/ask',
            data=json.dumps(test_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('status', data)
        self.assertIn('message', data)

if __name__ == '__main__':
    unittest.main()
