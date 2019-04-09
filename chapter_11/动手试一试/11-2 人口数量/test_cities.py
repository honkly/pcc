import unittest
from city_functions import get_formatted_name

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_city_country(self):
        full_name = get_formatted_name('beijing', 'china')
        self.assertEqual(full_name, 'beijing,china')

    def test_city_country_population(self):
    	full_name = get_formatted_name('beijing', 'china', population=1400000000)
    	self.assertEqual(full_name, 'beijing,china-population 1400000000')

unittest.main()
