"""Crie um sistema de registro de funcionarios em uma empresa,
onde diferentes tipos de funcionarios tem comportamentos especificos.
Crie uma classe funcionario generica com um metodo 'calcular salario'. Após, crie
subclases de funcionarios espeficos, como funcionarios CLT, funcionario Comissionado, funcionario Estagiario """

"""Crie um sistema que solicite e guarde os dados numa lista ou dicionario"""
"""Crie as instancias das classes"""

class Funcionario():
    def __int__ (self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
                
class Clt(Funcionario):
    def calcular_salario(self, base):
            return base
    
class Comissionado(Funcionario):
    def calcular_salario(self, comissao,venda):
        return  comissao * venda
    
class Estagiario(Funcionario):
    def calcular_salario(self, base):
        return base /2
    
funcionario_clt = Clt()
funcionario_comissionado = Comissionado()
funcionario_estagiario = Estagiario()


def sistema():
       
    funcionario = Funcionario()
    print (funcionario.calcular_salario())
    
sistema()
    
    



