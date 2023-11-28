# Importa as bibliotecas Selenium necessarias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#options = webdriver.ChromeOptions()
#options.add_argument('--disable-web-security')
#navegador = webdriver.Chrome(options=options)

# Instancia um navegador
navegador = webdriver.Chrome()

# Busca a URL digitando o termo
navegador.get("https://www.youtube.com/@Descomplicajogando")
time.sleep(3)

# Encontra um elemento na pagina, ex: Barra de login
elemento = navegador.find_element(By.CLASS_NAME,"yt-tab-shape-wiz__tab")



# Digita o e-mail 

#elemento.send_keys("marco_oneal@yahoo.com.br")

#elemento.send_keys(Keys.RETURN)
#time.sleep(3)

#elemento = navegador.find_element(By.CLASS_NAME,"VfPpkd-RLmnJb")
#elemento.click()