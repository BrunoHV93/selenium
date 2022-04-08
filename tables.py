#El objetivo de este ejercicio es obtener información contenida en una tabla y manipularla con Python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        #Para acceder la URL
        driver.get("http://the-internet.herokuapp.com/")
        #Para encontrar y dar click en el apartado correcto
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_sort_tables(self):
        driver = self.driver

        #Creamos una tabla vacía para guardar los datos. Se usa comprehension list para llenar de listas vacías
        table_data = [[] for i in range(5)]
        print(table_data)

        #Se itera para ir recorriendo los headers (columnas)
        for i in range(5):
            #Se usa el xpath porque contiene el número de elemento y nos sirve para iterar, sólo debemos convertir xpath a función 'f' 
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i+1}]/span')
            table_data[i].append(header.text)

            #Se extrae info de las filas
            for j in range(4):
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                table_data[i].append(row_data.text)


        print(table_data)





    def tearDown(self):
        #Se puede usar quit o close
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)