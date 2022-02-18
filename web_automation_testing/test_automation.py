import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC




#Inicializando Chrome
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/95.0.4638.54 Safari/537.36")
driver = webdriver.Chrome('web_automation_testing\chromedriver.exe', chrome_options=opts) 
driver.maximize_window()


#Identificando el url de la pagina
url = "https://www.demoblaze.com/"

#Abriendo la pagina
driver.get(url)


n = 0
productos = []
#Recorrido Horizontal (Por Categorias)
for i in range(1,4):
    
    #Identificando y seleccionando las Categorias
    categorias = ["Phones", "Laptops", "Monitors"]
    link = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/a[1+"'+str(i)+'"]')
    
    #Validando que entra a las categorias
    assert link.text == categorias[i-1], "No se encontro la categoria"
    time.sleep(1)
    link.click()
    time.sleep(1)
    index = [3,4,8,11,10,14]
    i = index[n]
    j = index[n+1]
    
    #Productos por categoria
    indice = [i,j]
    n+=2
    
    #Debugueando
    print("n es igual a: ", n)
    
    #Recorrido vertical (por producto)
    for elm in indice:
        link2 = driver.find_element_by_xpath('//a[@href="prod.html?idp_='+str(elm)+'"]')
        time.sleep(2)
        
        #Abriendo el producto en otra pagina
        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/95.0.4638.54 Safari/537.36")
        driver2 = webdriver.Chrome('web_automation_testing\chromedriver.exe', chrome_options=opts) 
        driver2.get(link2.get_attribute('href'))
        time.sleep(2)
        
        #Identificando el Boton de agregar al carrito
        button = driver2.find_element_by_xpath('//a[@class="btn btn-success btn-lg"]')
        
        #validando que el boton esta disponible
        assert button.text == "Add to cart", "No se encontro el boton de agregar a la carta"
        
        #Extrayendo el nombre del producto
        name = driver2.find_element_by_xpath('//*[@id="tbodyid"]/h2').text
        
        #Debugueando
        print("El nombre del producto es: ", name)
        
        #Agregando el nombre del producto a una lista de productos
        productos.append(name)
        
        #Dar click en el boton de agregar al carrito
        button.click()
        time.sleep(2)
        
        #Aceptando la alerta de "Product added"
        Alert(driver2).accept()
        time.sleep(1)
        
        #checkando que se agrego el producto a la carta
        cart = driver2.find_element_by_xpath('//*[@id="cartur"]')
        cart.click()
        time.sleep(3)
        driver2.quit()
time.sleep(1)

#Validando que el tamaño de la lista de productos sea igual a los productos que se agregaron a la carta 
assert len(productos) == 6, "No se encontro el numero de productos"
driver.quit()
