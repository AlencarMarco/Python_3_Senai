"""Crie uma classe chamada Pedido que permite criar objetos que representam pedidos em um restaurante
cada objeto de pedido deve conter informações como o nome do cliente, itens do pedido e o valor total"""

class Pedido:
    def __init__(self, cliente, itens, valor_total):
        self.cleinte = cliente
        self.itens = itens
        self.total = valor_total
