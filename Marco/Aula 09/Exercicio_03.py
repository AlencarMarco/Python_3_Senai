"""Crie uma classe pessoa que possui um atributo de classe para manter o numero de pessoas criadas. Cada vez que você instancia um objeto da classe pessoa, o contatod deve ser incrementado."""

class Pessoa:
    total_pessoas = 0 #atributo

    def __init__(self, nome, idade): #Metodo construtor
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1
        
pessoa1 = Pessoa("Marco", 33)
pessoa2 = Pessoa("Jessica", 32)
print(f"Total de pessoas: {Pessoa.total_pessoas}")





 