from unittest import (TestCase)
from app import app

class BloglyTest(TestCase):
    """Testing Blogly"""

    def test_users(self):
        with app.test_client() as client:
            res = client.get('/users')
            html = res.get_data(as_text=True)        
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)

    def test_details(self):
        with app.test_client() as client:
            res = client.get('/users/8')
            html = res.get_data(as_text=True)        
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Michael', html)

    def test_create_view(self):
        with app.test_client() as client:
            res = client.get('/users/new')
            html = res.get_data(as_text=True)        
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Add a User</h1>', html)

    def test_create(self):
        with app.test_client() as client:
            res = client.post('/users/new', data={'firstname': 'Michael', 'lastname': 'Murphy', 'userURL': 'http://michaeljmurphy.com/Michael_J_Murphy.jpg'})
            html = res.get_data(as_text=True)        
            self.assertEqual(res.status_code, 302)
            self.assertIn(res.location[:17], 'http://localhost/')
