#Este código automatiza la creación de un nuevo usuario en la página
#Automatización de form, textbox, checkbox y radio button

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)    

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        #Para presionar la opción login e ir a la página de creación de usuario nuevo
        driver.find_element_by_link_text('Log In').click()

        #Para encontrar botón de crear usuario
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        #Antes de presionar el botón es necesario ver si estpa habilitado
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        #Para dar click en el botón
        create_account_button.click()

        #Verificamos si el nombre de la pestaña tiene un nombre determinado
        self.assertEqual('Create New Customer Account', driver.title)

        #Se van a probar todos los campos a llenar. No se deben usar datos reales
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[1]/ul/li[4]/label')

        #Para verificar que los inputs estén habilitados
        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        #Para enviar datos a cada uno de los elementos
        #Se ponen pausas para ver cómo llena campos 
        first_name.send_keys('Test')
        driver.implicitly_wait(1)
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('Test')
        news_letter_subscription.send_keys('Test')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)