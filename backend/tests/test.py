import unittest
from backend.deployment.code.predict import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Churn Prediction API', response.data)

    def test_predict_endpoint(self):
        data = {
            "gender": "female",
            "seniorcitizen": 0,
            "partner": "yes",
            "dependents": "no",
            "phoneservice": "no",
            "multiplelines": "no_phone_service",
            "internetservice": "dsl",
            "onlinesecurity": "no",
            "onlinebackup": "yes",
            "deviceprotection": "no",
            "techsupport": "no",
            "streamingtv": "no",
            "streamingmovies": "no",
            "contract": "month-to-month",
            "paperlessbilling": "yes",
            "paymentmethod": "electronic_check",
            "tenure": 1,
            "monthlycharges": 29.85,
            "totalcharges": (24 * 29.85)
        }
        response = self.app.post('/predict', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'churn', response.data)

    def test_predict_endpoint_invalid_data(self):
        data = {"invalid_key": "invalid_value"}
        response = self.app.post('/predict', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'error', response.data)

    def test_predict_endpoint_missing_data(self):
        data = {"gender": "female"}
        response = self.app.post('/predict', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'missing data', response.data)

if __name__ == '__main__':
    unittest.main()
