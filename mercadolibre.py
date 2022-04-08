#Automatizacióndel sitio de mercado libre. El flujo será el siguiente:
#1.Ingresar a mercadolibre.com
#2.Seleccionar 'Colombia' como país
#3.Buscar el término "xbox series x"
#4. Filtrar por condición de "Nuevos"
#5.Filtrar por ubicación de "Bogotá"
#6.Ordenar de mayor a menor el precio
#7.Obtener el nombre y el precio de los primeros 5 artículos

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        #Para acceder la URL
        driver.get("http://mercadolibre.com/")

    def test_search_xbox(self):
        driver = self.driver

        #Ubicamos país y damos click
        country = driver.find_element_by_id('CO')
        country.click()

        sleep(3)

        #Acepta cookies
        cookies = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/button[1]')
        cookies.click()
        sleep(3)

        #Ubicamos barar de búsqueda
        search_bar = driver.find_element_by_name('as_word')
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys('xbox series x')
        search_bar.submit()

        sleep(3)

        #Ahora buscamos el filtro de 'Nuevo'
        new_filter = driver.find_element_by_css_selector('#root-app > div > div.ui-search-main.ui-search-main--only-products > aside > div.ui-search-filter-groups > div:nth-child(4) > ul > li:nth-child(1) > form > button > span.ui-search-filter-name')
        new_filter.click()

        sleep(3)
 
        #Buscamos filtro de ubicación
        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        location.click()

        sleep(3)

        #Ordenamos de mayor a menor
        order_menu = driver.find_elements_by_class_name('andes-dropdown__trigger')
        order_menu.click()

        # higher_price = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > div > ul > a:nth-child(3) > div.andes-list__item-first-column > div.andes-list__item-text > div')
        # higher_price.click()


        def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity = 2)
