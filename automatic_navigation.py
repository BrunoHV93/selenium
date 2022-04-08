#Automatización de navegación por google.com, haciendo back, fordward y refresh
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#Una manera de poner tiempos para visualizar la prueba es importando sleep pero no es recomendable porque agrega mucho tiempo a la ejecución
from time import sleep


class CompareProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://google.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)    

    def test_compare_products_removal_alert(self):
        #Se hace esto para no tener que estar poniendo self.driver en todo
        driver = self.driver

        #Para encontrar la barra de búsqueda
        search_field = driver.find_element_by_name('q')
        #Es buena práctica limpiar barra de búsqueda por si tiene algún texto
        search_field.clear()
        #Ahora ponermos lo que queremos buscar
        search_field.send_keys('platzi')
        #Enviamos
        search_field.submit()

        #Lo anterior nos manda a la página de resultados
        #Con esto retrocedemos a la página de búsqueda
        driver.back()
        sleep(1)

        #Avanzamos una página
        driver.forward()
        sleep(1)

        #Yo quise que búsqueda y pusiera otra cosa y refrescara antes de darle refresh
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('hola')
        sleep(1)
        driver.refresh()
        sleep(1)



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)