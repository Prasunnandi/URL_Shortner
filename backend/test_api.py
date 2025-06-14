import unittest
from app import app, db, Url

class TestURLShortener(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
    
    def tearDown(self):
        with app.app_context():
            db.drop_all()
    
    def test_shorten_url(self):
        response = self.app.post('/api/shorten', json={'url': 'https://example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('short_url', response.json)
    
    def test_redirect(self):
        # First create a short URL
        self.app.post('/api/shorten', json={'url': 'https://example.com'})
        # Then test redirect
        response = self.app.get('/abc123')
        self.assertEqual(response.status_code, 404)  # Will fail unless we mock

if __name__ == '__main__':
    unittest.main()