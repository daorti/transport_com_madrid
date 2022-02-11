

import unittest
from ayto_madrid.src.utils import read_config_file


class TestReadConfigFile(unittest.TestCase):
    def test_return_dict_type(self):
        return_type = dict
        self.assertEqual(type(read_config_file(
            '/Users/antoniojimenez/Desktop/Transports_Madrid/ayto_madrid/src/config.yml', None)),
            return_type)

    def test_abs_file_path(self):
        return_type = dict
        self.assertEqual(type(read_config_file(
            None, '/Users/antoniojimenez/Desktop/Transports_Madrid/ayto_madrid/src/config.yml')),
            return_type)



