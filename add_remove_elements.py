#En este reto se pretende añadir y remover elementos del un cierto sitio web que así lo permite
#Se utilizarán try and except para manejo de error
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://the-internet.herokuapp.com/")
        #Para encontrar y dar click en el apartado correcto
        driver.find_element_by_link_text('Add/Remove Elements').click()  


    #Es importante mencionar que el nombre de las pruebas siempre deben comenzar con test, sino no se ejecutan    
    def test_add_remove(self):
        driver = self.driver

        #Se pregunta al usuario cuantos elementos quiere agregar y cuantos remover
        elements_added = int(input('Elements to add: '))
        elements_removed = int(input('Elements to remove: '))

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("Can´t delete more elements than added")
                break


    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)