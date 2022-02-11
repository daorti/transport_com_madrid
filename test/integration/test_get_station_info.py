

import unittest
from ayto_madrid.src.utils import get_station_info


class TestStationInfo(unittest.TestCase):
    def test_int_input1_1(self):
        with self.assertRaises(TypeError):
            get_station_info(10, 10)

    def test_int_input1_2(self):
        with self.assertRaises(TypeError):
            get_station_info('EMT', '10')

    def test_bad_transportation(self):
        with self.assertRaises(ValueError):
            get_station_info('Metro', 155)

    def test_lowercase_transportation(self):
        return_type = dict
        self.assertEqual(type(get_station_info('bicimad', 151)),
                         return_type)

    def test_uppercase_transportation(self):
        return_type = dict
        self.assertEqual(type(get_station_info('EMT', 1514)),
                         return_type)


if __name__ == "__main__":
    unittest.main()

