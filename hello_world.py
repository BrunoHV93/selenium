#Primer programa e Selenium 

#Instalamos unittest para traer todas nuestras pruebas
import unittest 
#Para orquestar cada una de las pruebas
from pyunitreport import HTMLTestRunner
#Para comunicarnos con el navegador
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#Esta clase , que es nuestra prueba, hereda o hace referencia a unittest y TestCase que son nuestros casos de prueba.
class HelloWorld(unittest.TestCase):

    @classmethod
    #Esta sección ejecuta todo lo necesario antes de ejecutar una prueba, prepara entorno de la prueba misma.
    def setUp(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(10)

    #Caso o casos de prueba, donde se realizan una serie de acciones para que el navegador los automatice
    def test_hello_world(self):
        #Se pone esto para no tener que repetir el self.driver siempre que usemos driver
        driver = self.driver
        #Sin la línea de arriva se vería como self.driver.get...
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('http://www.wikipedia.org')

    @classmethod
    #Accciones para finalizar, por ejemplo, cerrar la ventana de navegador para evitar fuga de recursos o 
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
    