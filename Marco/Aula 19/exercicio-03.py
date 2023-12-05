#Exercicio 03 - Criar um script com pyautogui que digita um texto no bloco de notas, copia e cola o mesmo texto em outro bloco de notas

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
pyautogui.write("O segredo para começar bem o dia está em lembrar que cada manhã é uma nova oportunidade para sorrir, crescer, aprender e fazer a diferença")

#Espera 2 seg
time.sleep(3)

#salva o arquivo
pyautogui.hotkey('ctrl', 'a')

#Espera 2 seg
time.sleep(3)

#salva o arquivo
pyautogui.hotkey('ctrl', 'c')

#Abrir o programa
pyautogui.press('winleft')
programa = "Bloco de notas"
pyautogui.write(programa)
pyautogui.press('enter')

#Espera 2 seg
time.sleep(3)

#cola
pyautogui.hotkey('ctrl', 'v')