import unittest
import requests

class TestStringMethods(unittest.TestCase):

    URL = "http://127.0.0.1:5000"

    jsonData = {
        "user": "sia2602",
        "password": "Ola_mundo!"
    }

    def test_post(self):
        request = requests.post(f'{self.URL}/validate', json=self.jsonData)
        self.assertEqual(request.status_code, 200)

if __name__ == '__main__':
    unittest.main()