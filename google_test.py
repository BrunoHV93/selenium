#Este programa funciona con el programa google page, tiene como objetivo implementar POM para abstraer pruebas y hacerlas reutilizables.

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from google_page import GooglePage


class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_sort_tables(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)



    def tearDown(self):
        #Se puede usar quit o close
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)