import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Clase de caso de prueba
class searchTest(unittest.TestCase):
    #Método que prepara lo necesario para la prueba
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        #Para ir a sitio web
        driver.get("http://demo-store.seleniumacademy.com/")
        #Para maximizar la ventana porque elementos pueden cambiar en diferentes vistas (Responsive)
        driver.maximize_window()
        driver.implicitly_wait(15)

    #Aquí encuentra un elemento en el sitio web cuyo id sea search. 
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    #Aquí encuentra un elemento en el sitio web cuyo nombre sea q, nombre que vimos al inspeccionar sitio.
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    #Para encontrar elemento por nombre de clase
    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")

 

    #Cuando un elemento no tiene un identificador explícito podemos usae xpath, al cual accedemos en la opciones de copiado.
    #Puede  no ser la mejor opción porque al cambiar el sitio cambia elxpath
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a/img')

    #Para encontrar por selector en css
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)