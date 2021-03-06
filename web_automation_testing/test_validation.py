import unittest
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class TestAutomation(unittest.TestCase):
    def setUp(self):
        #Inicializando Chrome
        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/95.0.4638.54 Safari/537.36")
        self.driver = webdriver.Chrome('web_automation_testing\chromedriver.exe', chrome_options=opts) 
        self.driver.maximize_window()

    def test_automation(self):
        #Identificando el url de la pagina
        url = "https://www.demoblaze.com/"

        #Abriendo la pagina
        self.driver.get(url)

        n = 0
        productos = []
        #Recorrido Horizontal (Por Categorias)
        for i in range(1,4):
            #Identificando y seleccionando las Categorias
            categorias = ["Phones", "Laptops", "Monitors"]
            link = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/a[1+"'+str(i)+'"]')
            time.sleep(6)
            
            #Validando que entra a las categorias
            self.assertEqual(link.text, categorias[i-1], "No se encontro la categoria")
            time.sleep(1)
            try:
                link.click()
                time.sleep(1)
            except WebDriverException as e:
                print("No se pudo abrir la pagina de la categoria: ", categorias[i-1])
                print(e)
                time.sleep(1)

            #Indexando los productos por seleccionar
            index = [3,4,8,11,10,14]
            i = index[n]
            j = index[n+1]

            #Productos por categoria
            indice = [i,j]
            n+=2

            #Debugueando
            print("n es igual a: ", n)

            #Recorrido vertical (por productos)
            for elm in indice:
                link2 = self.driver.find_element_by_xpath('//a[@href="prod.html?idp_='+str(elm)+'"]')
                time.sleep(2)
                
                #Abriendo el producto en otra pagina
                opts = Options()
                opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/95.0.4638.54 Safari/537.36")
                self.driver2 = webdriver.Chrome('web_automation_testing\chromedriver.exe', chrome_options=opts) 
                self.driver2.get(link2.get_attribute('href'))
                time.sleep(2)
                
                #Identificando el Boton de agregar al carrito
                button = self.driver2.find_element_by_xpath('//a[@class="btn btn-success btn-lg"]')
                
                #validando que el boton esta disponible
                self.assertEqual(button.text, "Add to cart", "No se encontro el boton de agregar al carrito")
                
                #Extrayendo el nombre del producto
                name = self.driver2.find_element_by_xpath('//*[@id="tbodyid"]/h2').text
                
                #Debugueando
                print("El nombre del producto es: ", name)
                
                #Agregando el nombre del producto a una lista de productos
                productos.append(name)
                
                #Dar click en el boton de agregar al carrito
                try:
                    button.click()
                    time.sleep(2)
                except WebDriverException as e:
                    print("No se pudo agregar el producto: ", name)
                    print(e)
                    time.sleep(2)
                
                #Validando que se agrega el producto a la carta
                self.assertEqual(Alert(self.driver2).text, "Product added", "No se encontro el mensaje de producto agregado")
                
                #Aceptando la alerta de "Product added"
                Alert(self.driver2).accept()
                time.sleep(1)
                
                #checkando que se agrego el producto a la carta
                cart = self.driver2.find_element_by_xpath('//*[@id="cartur"]')
                cart.click()
                time.sleep(3)
                self.driver2.close()
        time.sleep(1)
        #Validando que el tama??o de la lista de productos sea igual a la cantidad de  productos que se agregaron a la carta 
        self.assertEqual(len(productos), 6 , "No se encontro la cantidad de productos en la carta")
        self.driver.close()
                
                
if __name__ == '__main__':
    unittest.main()              