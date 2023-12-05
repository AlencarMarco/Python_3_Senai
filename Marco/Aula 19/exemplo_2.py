import pyautogui
import time
#Função para desenhar estrela
def desenhar_estrela(x,y,tamanho):
    pyautogui.click(x,y) #Clica no ponto inicial no Paint

    #abrir o programa
    pyautogui.press('winleft')
    programa = "Paint"
    pyautogui.write(programa)
    pyautogui.press('enter')

    #Calcular os pontos da estrela
    pontas = 5
    angulo = 360 / pontas
    raio_externo = tamanho
    raio_interno = tamanho/2

    for i in range(pontas*2):
        if 1 % 2 ! = 0:
            pyautogui.dragRel(raio_interno,0, duration=1)
            #Deseneha a linha interna

        else:
            pyautogui.dragRel(raio_externo,0, duration=1)
            #desenha a linha externa

        pyautogui.moveRel(0,0)

    #Aguardar alguns segundos
    time.sleep(5)

    #coordenadas do ponto inicial e tamanho da estrela
    x_inicial, y_inicial,

#Exercicio 01 - Faça uma altomalçao com pyautogui, pela qual o programa abra o bloco de notas, digita uma mensagem e salve o arquivo 