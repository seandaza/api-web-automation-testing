from email import message
from itertools import product
from tkinter import Button
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




headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
           "referer": "https://www.fincaraiz.com.co/"
}


#Creando conexion con MongoDB:

''' #Instanciamos el cliente de MongoDB
client = MongoClient('localhost', 27017)
#Instanciamos la base de datos
db = client['nombre_base_de_datos']
#Instanciamos la coleccion
col = db['nombre de coleccion'] '''


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
for i in range(1,4):
    i = str(i)
    #Identificando y seleccionando las Categorias
    link = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/a[1+"'+i+'"]')
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
        i = str(elm)
        link2 = driver.find_element_by_xpath('//a[@href="prod.html?idp_='+i+'"]')
        time.sleep(2)
        #Abriendo el producto en otra pagina
        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/95.0.4638.54 Safari/537.36")
        driver2 = webdriver.Chrome('web_automation_testing\chromedriver.exe', chrome_options=opts) 
        driver2.get(link2.get_attribute('href'))
        #Agregando el producto a la carta
        time.sleep(2)
        button = driver2.find_element_by_xpath('//a[@class="btn btn-success btn-lg"]')
        button.click()
        time.sleep(1)
        driver2.quit()
time.sleep(1)
driver.quit()