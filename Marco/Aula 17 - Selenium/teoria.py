#importar biblioteca selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys


#instanciar um navegador(Chrome, firefox e outros neste usaremos o Chrome)

navegador = webdriver.Chrome()

#Navegar para um URL

#navegador.get("https://www.anhanguera.com/inscricao/")

#time.sleep(3)

navegador.get("https://www.google.com.br/")

try: # Encapsula um codigo que pode gerar erro
    time.sleep(2) #aguarda 2 segundos

    #Encontrar um elemento pelo ID

    elemento = navegador.find_element(By.ID,"APjFqb")

    #elemento.click()

    elemento.send_keys("Greve de Metro em São Paulo") 


    elemento.send_keys(Keys.RETURN)
    time.sleep(3)

finally:
    #fecha o navegador
    navegador.close()
