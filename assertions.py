import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Nos servirá como una excepción para nuestros asserts cuando queramos validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException

#Nos ayuda a llamar a las excepciones que queremos validar
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    #Para verificar que campo de busqueda está presente
    def test_search_field(self):
        self.assertTrue(self.is_elemet_present(By.NAME, 'q'))
    
    #Para verificar elemento de cambio de lenguaje en sitio web
    def test_language_option(self):
        self.assertTrue(self.is_elemet_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    #Función de utilidad para identificar cuando un elemento está presente
    #How es para indicar tipo de selector y what el valor que tiene
    def is_elemet_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True