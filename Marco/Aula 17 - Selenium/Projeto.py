"""entrar no site da Anhanguera, escolher o 
curso de ADM, Continuar inscrisção, e preencher com os dados, gerador de CPF gerar cpF copiar e colocar no site da anhaguera"""

#importar as bibliotecas Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get("https://www.anhanguera.com/")

elemento = navegador.find_element(By. ID,"open-inscricao")
elemento.click()
time.sleep(1.5)

elemento_curso_adm = navegador.find_element(By.XPATH, '//*[@id="course-bc0e9fe153a4f760ee51f8f52b41b0bf"]')
elemento_curso_adm.click()

time.sleep(2)

elemento_continuar_inscricao = navegador.find_element(By.XPATH, '//*[@id="vueApp"]/footer/button' )
elemento_continuar_inscricao.click()

time.sleep(2)

navegador.find_element(By.ID, "nome").send_keys("Seu Nome")
navegador.find_element(By.ID, "email").send_keys("seu.email@example.com")







