class Calculadora:
    def soma(self, num1, num2,):
        return num1 + num2

    def subtracao(self, num1, num2,):
        return num1 - num2

    def multiplicacao(self, num1, num2,):
        return num1 * num2

    def divisao(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Divisão por zero não é permitida."

# Exemplo de uso:
calculadora = Calculadora()
print("Soma:", calculadora.soma(5, 3))               # Saída: 8
print("Subtração:", calculadora.subtracao(10, 4))    # Saída: 6
print("Multiplicação:", calculadora.multiplicacao(6, 7))  # Saída: 42
print("Divisão:", calculadora.divisao(8, 2))        # Saída: 4.0
print("Divisão por zero:", calculadora.divisao(5, 0))  # Saída: Divisão por zero não é permitida.