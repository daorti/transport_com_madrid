

import unittest
from ayto_madrid.src.utils import get_distance


class TestGetDistance(unittest.TestCase):
    def test_not_iterable_1(self):
        with self.assertRaises(TypeError):
            get_distance([1.0, 1.0], 1)

    def test_not_iterable_2(self):
        with self.assertRaises(TypeError):
            get_distance(1, [1.0, 1.0])

    def test_not_float_1(self):
        with self.assertRaises(TypeError):
            get_distance([1, 1.0], [1.0, 1.0])

    def test_not_float_2(self):
        with self.assertRaises(TypeError):
            get_distance([1.0, 1], [1.0, 1.0])

    def test_not_float_3(self):
        with self.assertRaises(TypeError):
            get_distance([1.0, 1.0], [1, 1.0])

    def test_not_float_4(self):
        with self.assertRaises(TypeError):
            get_distance([1.0, 1.0], [1.0, 1])

    def test_return_string(self):
        return_type = str
        self.assertEqual(type(get_distance([1.0, 1.0], [1.0, 1.0])),
                         return_type)


if __name__ == "__main__":
    unittest.main()