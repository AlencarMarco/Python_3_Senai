#Exercicio 01 - Faça uma altomalçao com pyautogui, pela qual o programa abra o bloco de notas, digita uma mensagem e salve o arquivo 
#Exercicio 02 - Cria um script ocm pyautogui que abre o navegador, digita e pesquisa, entra no site e fecha o navegador

import pyautogui
import time

   
#Abrir o programa
pyautogui.press('winleft')
programa = "Bloco de notas"
pyautogui.write(programa)
pyautogui.press('enter')

#Espera 2 seg
time.sleep(3)

#Digita uma mensagem
pyautogui.write("Amanhã tem GTA6")

#Espera 2 seg
time.sleep(3)

#salva o arquivo
pyautogui.hotkey('ctrl', 's')

#Digita uma mensagem
pyautogui.write("arquivo.txt")

pyautogui.hotkey('enter')