#Este programa tiene como objetivo comparar si un cierto texto concuerda con el del sitio web
#Es como hacer un pequeño webscrapping, aunque  Selenium no es para eso
#En el sitio web el texto cambia y pone errores cada que se refresca
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        #Para acceder la URL
        driver.get("http://the-internet.herokuapp.com/")
        #Para encontrar y dar click en el apartado correcto
        driver.find_element_by_link_text('Typos').click()

    def test_find_typos(self):
        driver = self.driver

        #Para ubicar el texto que queremos comparar
        paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')

        #Para extraer el texto
        text_to_check = paragraph_to_check.text
        #Podemos verificar lo que estamos copiando con un print
        print(text_to_check)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        #Para evitar que texto sea el equivocado
        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            driver.refresh()

        while not found:
            if text_to_check == correct_text:
                tries += 1
                driver.refresh()
                found = True

        #Para mensaje de salida
        self.assertEqual(found, True)
        print(f"It took {tries} tries to found the typo")




    def tearDown(self):
        #Se puede usar quit o close
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)