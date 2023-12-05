"""Exercicio 04 - Crar um scipt com selenium e pyautogui que pesquisa sobre um tema no gooogle, 
copia e cola o titulo no bloco de notas e o salva."""

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Instancia um navegador
navegador = webdriver.Chrome()

# Busca a URL digitando o termo
navegador.get("http://google.com")

#Espera 3seg
time.sleep(3)

#pesquisa
pyautogui.write("Game of thrones")
pyautogui.press("enter")
#localiza o texto

#Espera 3seg
time.sleep(3)

#Encontra um elemento na pagina, ex: Barra de login
elemento = navegador.find_element(By.ID,"APjFqb")
texto_elemento = elemento.text

#Espera 2 seg
time.sleep(3)

#Abrir o programa
pyautogui.press('winleft')
programa = "bloco de nota"
pyautogui.write(programa)
pyautogui.press('enter')

#Espera 2 seg
time.sleep(3)

#Digita uma mensagem
pyautogui.write(texto_elemento)
pyautogui.press('enter')

time.sleep(5)

#Salva o documento
pyautogui.hotkey("ctrl","s")




