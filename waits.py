#Uso de demoras
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Importamos By para hacer referencia a un elemento del sitio mediante selectores, no a ubicarlo, sino a interactuar con él
#distinto a como lo hace drover
from selenium.webdriver.common.by import By

#Importamos WebDriverWair para hacer uso de las esperas explícita.
from selenium.webdriver.support.ui import WebDriverWait
#Para usar las expected conditions. Se importa como EC para abreviar
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWaitTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)    

    def test_account_link(self):
        #Para esperar 10 segundos hasta que se cumpla nuestra función esperada.
        #En este caso la función esperada es encontrar el menú de idiomas y contar que tenga 3 elementos
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        #Hacemos referencia a donde están las cuentas
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))

        #Hacer click en account
        account.click()



    def test_create_new_customer(self):
        #Para encontrar elemento por texto y darle click
        self.driver.find_element_by_link_text('ACCOUNT').click()

        #Para esperar
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        #Para dar click
        my_account.click()

        #Para esperar condición a verificar que elemento sea clickeable
        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        #Para dar click al botón
        create_account_button.click()

        #Para verificar que título contiene un cierto texto
        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)