def custo_mercadoria_vendida(estoque_nicial, estoque_final, compras):
    cmv = estoque_final + compras - estoque_inicial
    print("O estoque atual é de: ", cmv)

def valor_compras_periodo(estoque_inicial, estoque_final):
    valor_compras_peiodo = estoque_final- estoque_inicial
    print("O valor compras: ", valor_compras_periodo)

def custo_mercadoria_vendida():