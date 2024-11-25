import unittest
from app import app
import json

class ForexConverterTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_currency_conversion(self):
        response = self.app.post('/', data=dict(
            from_currency='USD',
            to_currency='EUR',
            amount='10'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Result:', response.data)

    def test_missing_currency(self):
        response = self.app.post('/', data=dict(
            from_currency='',
            to_currency='EUR',
            amount='10'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error: Please provide both', response.data)

    def test_invalid_currency_code(self):
        response = self.app.post('/', data=dict(
            from_currency='XYZ',
            to_currency='EUR',
            amount='10'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error:', response.data)

    def test_invalid_amount(self):
        response = self.app.post('/', data=dict(
            from_currency='USD',
            to_currency='EUR',
            amount='invalid'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error:', response.data)

if __name__ == '__main__':
    unittest.main()
