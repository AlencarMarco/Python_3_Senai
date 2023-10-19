"""Crie uma classe tarefa que representa uma tarefa a ser realizada. A classe deve ter atributos como nome da tarefa
data de vencimento e status(pendente, em andamento, concluida). Implemente metodos para marcar a tarefa"""

class Tarefa:
    def __init__(self, nome, prazo):
        self.nome = nome
        self.prazo = prazo
        self.status = "Pendente"

    def marcar_concluido(self):
        self.status = "Concluida"

    def verificar_vencimento(self):
        data_tarefa = input("Digite a data da tarefa: ")
        if self.status == "Pendente" and self.prazo < data_tarefa:
          return f"A tarefa '{self.nome}' esta atrasada"
        
        return f"A tarefa '{self.nome}' está em dia"
    
tarefa01 = Tarefa("Passear com o cachorro", "18/10/2023")

print(tarefa01.verificar_vencimento())
print(tarefa01.status)


