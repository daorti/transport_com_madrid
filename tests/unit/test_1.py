import unittest
from src.utils import check_empty_dataset, charging_dataset
from src.emt_strategy import EMT
import pandas as pd


class TestUtils(unittest.TestCase):
    def test_empty_dataset(self):
        empty = pd.DataFrame()
        df = pd.read_csv('./data/bicimad_df_cleaned.csv', sep=',', dtype=str)
        self.assertEqual(check_empty_dataset(df), 'The search has results')
        with self.assertRaises(TypeError):
            check_empty_dataset(empty)
        self.assertEqual(check_empty_dataset(1), 'Not a dataframe')

    def calculate_distances(self):
        transport = EMT(charging_dataset(), 'Ayala', 92, "-3.695302462399076, 40.43245797647746")
        self.assertIsInstance(transport.calculate_distances(), obj=float)

if __name__ == "__main__":
    unittest.main()