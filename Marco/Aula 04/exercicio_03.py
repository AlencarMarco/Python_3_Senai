"""Condição do exercicio: Jogo, adivinhe o numero, o usuario vai digintado numeros "Função: randon", numero maior - "Numero digitado é menor", Numero menor -"O numero é maior" """
import random
numero_Sorteado = random.randint(1,100)
tentativas = 0

while (True):
    tentativa = int (input("Adivinhe o número de 1 a 100: "))
    tentativas += 1

    if (tentativa == numero_Sorteado):
      print(f"você acertou em {tentativas} tentativas.")
      break

    elif (tentativa < numero_Sorteado):
      print("O numero é maior")
      
    else: 
      print("O numero é menor")
      
     
