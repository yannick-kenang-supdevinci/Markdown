import unittest
from health_utils import calculate_bmi, calculate_bmr
from app import app
import json

class TestHealthUtils(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_calculate_bmi(self):
        # Test normal case
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        
        # Test error cases
        with self.assertRaises(ValueError):
            calculate_bmi(-1.75, 70)
        with self.assertRaises(ValueError):
            calculate_bmi(1.75, -70)

    def test_calculate_bmr_male(self):
        # Test normal case for male
        self.assertAlmostEqual(
            calculate_bmr(175, 70, 25, 'male'),
            1724.05,
            places=2
        )

    def test_calculate_bmr_female(self):
        # Test normal case for female
        self.assertAlmostEqual(
            calculate_bmr(160, 60, 30, 'female'),
            1368.19,
            places=2
        )

    def test_bmi_endpoint(self):
        # Test successful BMI calculation
        response = self.app.post('/bmi',
            json={'height': 1.75, 'weight': 70}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(data['bmi'], 22.86, places=2)

        # Test missing data
        response = self.app.post('/bmi', json={})
        self.assertEqual(response.status_code, 400)

    def test_bmr_endpoint(self):
        # Test successful BMR calculation
        response = self.app.post('/bmr',
            json={
                'height': 175,
                'weight': 70,
                'age': 25,
                'gender': 'male'
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('bmr', data)
        self.assertIn('daily_calories', data)

        # Test missing data
        response = self.app.post('/bmr', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
