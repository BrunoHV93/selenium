#Automatización de alert y pop-up
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CompareProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)    

    def test_compare_products_removal_alert(self):
        #Se hace esto para no tener que estar poniendo self.driver en todo
        driver = self.driver
        #Sin la declaración de arriba tendriamos que poner self.driver.find_element...
        #Para buscar barra de navegación
        search_field = driver.find_element_by_name('q')
        #Como buena práctica se limpia el texto que haya en las barras de búsquedas
        search_field.clear()

        #Se busca en la barra de navegación las playeras
        search_field.send_keys('tee')
        search_field.submit()

        #Ahora se identifica elemento de comparar
        driver.find_element_by_class_name('link-compare').click()
        #Ahora se busca enlace para limpiar lista de comparación y hacer aparecer el pop up alert
        driver.find_element_by_link_text('Clear All').click()

        #Se crea variable para alert
        #Se indica al driver que cambie la atención hacia el alert
        alert = driver.switch_to.alert
        alert_text = alert.text

        #Para validar que texto de alerta sea igual al deseado
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        #Para presionar el botón de aceptar
        alert.accept()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)