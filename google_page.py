#Este programa funciona en conjunto con el programa google_test.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
#Llamamos expected conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as encontrar

#Clase de pruebas
class GooglePage(object):
    def __init__(self, driver):
        self._driver = driver
        #Para acceder al sitio
        self._url = 'http://google.com'
        #Para ubicar barra de búsqueda
        self.search_locator = 'q'

    #Para verificar que sitio cargó
    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True

    #Para búsqueda
    @property
    def keyword(self):
        input_field = self._driver.find_element_by_name('q')
        return input_field.get_attribute('value')

    #Métodos con los que trabajará este page object
    def open(self):
        self._driver.get(self._url)

    def type_search(self, keyword):
        input_field = self._driver.find_element_by_name('q')
        input_field.send_keys(keyword)

    def click_submit(self):
        input_field = self._driver.find_element_by_name('q')
        input_field.submit()

    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()