import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Importamos algunos módulos de DDT. Fue necesario instalar dtt con pip
from ddt import ddt, data, unpack

#Agregamos decorador
@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10) 

    #Agregamos decorador de datos a ingresar y resultado esperado
    @data(('dress', 5), ('music',5))
    #Para desempacarlos
    @unpack 

    def test_search_dtt(self, search_value, expected_count):
        driver = self.driver
        #Para encontrar barra de navegación
        search_field = driver.find_element_by_name('q')
        #Limpiamos barra de navegación
        search_field.clear()
        #Ingresamos información pero ahora desde search value, que son los datos que pusimos en el decorador data
        search_field.send_keys(search_value)
        #Enviamos
        search_field.submit()

        #Ahora identificamos los resultados. Notar que es find ELEMENTS y no ELEMENT
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        #Comparamos entrada con resultado
        self.assertEqual(expected_count, len(products))


    def tearDown(self):
        #Se puede usar quit o close
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)