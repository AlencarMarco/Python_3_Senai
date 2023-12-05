#Exercicio 02 - Cria um script com pyautogui que abre o navegador, digita e pesquisa, entra no site e fecha o navegador

import pyautogui
import time

#Abrir o programa
pyautogui.press('winleft')
programa = "Chrome"
pyautogui.write(programa)
pyautogui.press('enter')

#Espera 2 seg
time.sleep(3)

#Digita uma mensagem
pyautogui.write("interacademybrazil.com.br")
pyautogui.press('enter')

time.sleep(5)

#fecha o programa
pyautogui.hotkey('alt', 'f4')


