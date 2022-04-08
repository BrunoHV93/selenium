#Automatización de menú dropdown y listas
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#Para manipular dropdown es necesario importar
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)    

    def test_select_language(self):
        #Para tener nuestras opciones posibles
        exp_options = ['English', 'French', 'German']
        #Para guardar las opciones que vayamos eligiendo
        act_options = []

        #Para acceder a opciones de dropdown usamos el select, hay que decirle cómo encontrarlo
        select_language = Select(self.driver.find_element_by_id('select-language'))

        #Para validar que el ropdown tiene 3 opciones. El método options permite ingresar a las opciones del dropdown
        self.assertEqual(3, len(select_language.options))

        #Iteramos por cada una de las opciones que tenemos en el dropdown
        for option in select_language.options:
            act_options.append(option.text)
        
        #Para verificar que opciones expuestas y activas sean iguales
        self.assertListEqual(exp_options, act_options)

        #Para verificar que la primera opción es English
        self.assertEqual('English', select_language.first_selected_option.text)

        #Para seleccionar el idioma German
        select_language.select_by_visible_text('German')

        #Para verificar que cambie idioma, veridicando con parametro del url
        self.assertTrue('store=german' in self.driver.current_url)

        #También se puede seleccionar el idioma por el índice, se le indica cómo encontrarlo y después qué índice queremos que tome
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)