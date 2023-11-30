import requests
from bs4 import BeautifulSoup

def pesquisar_produto():
    
    produto_pesquisa = input("Qual produto você está procurando: ")
    
    # Substituir os espaços por '+' para formatar corretamente a URL
    produto_pesquisa = produto_pesquisa.replace(' ', '+')

    #chama o site 
    url = f'https://www.amazon.com.br/{produto_pesquisa}'

    # Enviar uma solicitação GET para a página de pesquisa
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, "html.parser")

        resultados = soup.find_all('li', class_ = 'ui-search-layout__item')
        



