#Este programa usa DDT pero trayendo datos desde un archivo CSV
#Necesario importar la librería CSV
import csv, unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Importamos algunos módulos de DDT. Fue necesario instalar dtt con pip
from ddt import ddt, data, unpack

#Agregamos una nueva función para obtener datos

def get_data(file_name):
    #Para filas
    rows = []

    #Para abrir archivo
    data_file = open(file_name, 'r')

    #Para leer
    reader = csv.reader(data_file)

    #Para pasar a la siguiente fila y omitir cabecera
    next(reader, None)

    for row in reader:
        rows.append(row)
    return rows

#Agregamos decorador
@ddt
class SearchCsvDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10) 

    @data(*get_data('testdata.csv'))
    @unpack

    def test_search_dtt(self, search_value, expected_count):
        driver = self.driver
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
        
        #Para pasar a entero el valor proveniente del CSV y no caer en errores
        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)

        print(f'Found {len(products)} products')


    def tearDown(self):
        #Se puede usar quit o close
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)