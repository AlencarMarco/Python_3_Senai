"""Criar uma aplicação, de locação de filmes, series e documentarios. 
Personagem chamado - Banco, Personagem - cartão de credito, Personagem - Locação, Personagem - Catalogo, Personagem - login """

class Veiculo: 
    def __init__(self, nome, marca, modelo, potencia, combustivel, n_passageiros):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.combustivel = combustivel
        self.n_passageiros = n_passageiros

class Automovel(Veiculo):
    def __init___(self, nome, marca, modelo, potencia, combustivel, n_passageiros, cor)
        self.cor = cor

        super(). __init__(self, nome, marca, modelo, potencia, combustivel, n_passageiros)
            
class Pessoa:
    def __init__(self, nome, sobrenome, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, endereco, matricula, curso):
        self.matricula = matricula
        self.curso = curso

        super(). __init__(self, nome, sobrenome, endereco)
