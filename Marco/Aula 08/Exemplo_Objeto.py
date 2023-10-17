"""class Automovel: #nome de classe sempre em MAIUSCULA
    def __init__(self, modelo, marca, cor): 
        self.modelo = modelo #CLASSE RECEBE MODELO QUE TEM VALOR EM MODELO
        self.marca = marca
        self.cor = cor

    def acelerar():
        return print("Vrum, Vrum")

automovel_1 = Automovel("Mustang","Ford","Azul")

automovel_1.acelerar()"""

class Retangulo: #Essa é a forma do objeto
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcula_area(self, base, altura): #Esse é o Metodo do objeto
        base = int(input("Digite a base: "))
        altura = int(input("Digite a altura: "))
        print(f"A área do retângulo é {base * altura}")

retangulo_1 = Retangulo(15,2)

retangulo_1.calcula_area(15,2)






