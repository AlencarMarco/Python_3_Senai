from model import Tarefas, ListaTarefaModelo
from view import ListaTarefasVisao

class ListaTarefasController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def adicionar_tarefa(self, descricao):
        tarefa = Tarefas(descricao)
        self.model.adicionar_tarefa(tarefa)

    def mostrar_tarefa(self):
        tarefa = self.model.obter_tarefa()
        self.view.mostrar_tarefa(tarefa)

    def executar(self):
        while True:
            self.view.mostrar_mensagem("\n Escolha uma opção: ")
            self.view.mostrar_mensagem("\n 1. Adicionar Tarefa: ")
            self.view.mostrar_mensagem("\n 2. Mostrar Tarefa: ")
            self.view.mostrar_mensagem("\n 3. Sair")

            escolha = self.view.obter_entrada_usuario("Digite o número da opção desejada")  

            if escolha == "1":
                descricao = self.view.obter_entrada_usuario("Digite a descrição da tarefa:")
                self.adicionar_tarefa(descricao)

            elif escolha == "2":
                self.mostrar_tarefa()

            elif escolha == "3":  # Corrigir a escolha para "3"
                self.view.mostrar_mensagem("Saindo do programa")
                break
