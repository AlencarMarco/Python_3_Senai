#Programa que o usuario entre com uma frase, e devolva com letras maiusculas, minuscula e separada por lista

frase = (input("Digite a sua frase: \n "))

print("Sua frase em maiuscula: \n" , frase.upper())
print("Sua frase em minusculo: \n" , frase.lower())
print("Sua frase separada por palavra: \n" , frase.split())
print("aqui esta sua frase: \n" , frase.capitalize())