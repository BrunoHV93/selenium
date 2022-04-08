#El objetivo de este programa es contar cuántos refresh son necesarios hasta encontrar el elementos dinámico
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class DynamicElement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        #Para acceder la URL
        driver.get("http://the-internet.herokuapp.com/")
        #Para encontrar y dar click en el apartado correcto
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_element(self):
        driver = self.driver
        element_found = 0
        element_status = False
        counter = 0

        while element_found == 0:
            try:
                gallery_element = driver.find_element_by_xpath('//*[@id="content"]/div/ul/li[5]/a')
                element_status = True
            except:
                element_status = False

            if element_status:
                element_found = 1
                counter += 1
            else:
                element_found = 0
                driver.refresh()
                counter += 1

        sleep(10)
        print(f'Element founded in round {counter}')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)