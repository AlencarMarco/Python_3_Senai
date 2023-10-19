"""Crie uma classe calculadora que possui para adicionar, subtrair, multiplicar e dividir dois numeros"""

class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
       
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
           return "Não é possivel dividir"
        return a / b
    


