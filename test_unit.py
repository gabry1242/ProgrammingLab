import unittest
from lezione5 import CSVFile

class TestCSVFile(unittest.TestCase):
    def test_init(self):
        csv_file = CSVFile('shampoo_sales.csv')
 # Controllo che il nome del file sia stato salvato
 # in un attributo dell’oggetto di nome “name”
        self.assertEqual(csv_file.name, 'shampo_sales.csv')