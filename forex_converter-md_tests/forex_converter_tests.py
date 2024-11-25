import unittest
from app import app

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

if __name__ == '__main__':
    unittest.main()
