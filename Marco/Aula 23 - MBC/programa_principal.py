from model import ListaTarefaModelo
from view import ListaTarefasVisao
from controler import ListaTarefasController

def principal():
    model = ListaTarefaModelo()
    view = ListaTarefasVisao()
    controller = ListaTarefasController(model, view)
    controller.executar()

principal()



