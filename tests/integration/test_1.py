import unittest
from src.utils import charging_dataset, creating_transport_object, check_empty_dataset
from src.bicimad_strategy import BICIMAD
import pandas as pd

name = 'Ayala'
id = '92'
coordinates = "-3.695302462399076, 40.43245797647746"
bicimad = pd.read_csv('./data/bicimad_df_cleaned.csv', sep=',', dtype=str)


class TestUtils(unittest.TestCase):

    def test_integration_with_results(self):
        transport = BICIMAD(bicimad, name, id, coordinates)
        self.assertEqual(check_empty_dataset(bicimad), 'The search has results')

        self.assertEqual(len(transport.find_station()), 1)
        self.assertEqual(len(transport.display_info()), 1)


    def test_integration_with_no_results(self):
        name = 'fsdgsdfg'
        id = '0'
        transport = BICIMAD(bicimad, name, id, coordinates)
        self.assertEqual(check_empty_dataset(bicimad), 'The search has results')

        self.assertEqual(len(transport.find_station()), 0)
        self.assertEqual(len(transport.display_info()), 0)


if __name__ == "__main__":
    unittest.main()