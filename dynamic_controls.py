#El objetivo de este ejercicio es utilizar tiempos de espera para permitir que carguen elementos y
#posteriormente usarlos
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Importamos módulos de espera, expected condition y By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        #Para acceder la URL
        driver.get("http://the-internet.herokuapp.com/")
        #Para encontrar y dar click en el apartado correcto
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamic_controls(self):
        driver = self.driver

        #--------------------------------------Para sección de checkbox------------------------------------------
        
        #El primer elemento a encontrar será el checkbox, copiaremos su selector de css
        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        #Para presionar
        checkbox.click()

        #Ahora ubicamos el botón de remover por su selector de CSS, se usan estos selectores para hacer cóigo más 
        #legible y prolijo 
        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
        #Hacemos click
        remove_add_button.click()

        #Cuando damos click al botón de remover, tarda un momento en desaparecer el checkbox, por lo que hay que
        #hacer una espera y esperar una condición, que el elemento de añadir (add) sea clickeable
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        #Una vez que esperamos, aparece el botón de añadir y damos click, se usa el mismo de remove porque tienen
        #el mismo selector CSS
        remove_add_button.click()

        #--------------------------------------Para sección de textarea--------------------------------------------
        #Ubicamos botón de Enable
        enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
        #Damos click
        enable_disable_button.click()

        #Esperamos a que se oculte el textarea
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > input[type=text]')))
        #Identificamos textarea
        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        #Para poner un texto
        text_area.send_keys('Hola')

        #Hora presionamos de nuevo el botón para desabilitar text área
        enable_disable_button.click()


    def tearDown(self):
        #Se puede usar quit o close
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)