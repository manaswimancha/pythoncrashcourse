from city_functions import city_country
import unittest

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country("santiago","chile"),"Santiago, Chile")
    def test_city_country_population(self):
        self.assertEqual(city_country("santiago","chile","10000"),"Santiago, Chile - population 10000")

if __name__ == "__main__":
    unittest.main()