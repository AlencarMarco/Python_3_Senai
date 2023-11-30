#Importar o BS4
from bs4 import BeautifulSoup
import requests

#URL da  página web a ser raspada

url = 'https://www.mercadolivre.com.br/'

#Enviar uma solicitação GET para a pagina

response = requests.get(url)

#Verificar se a solicitação foi bem sucedida
if response.status_code == 200:

    #Criar um objeto BS para analisar o nosso conteuto html da pagina
    soup = BeautifulSoup(response.text, 'html.parser')

    #Procura o primeiro elemento h1
    h1 = soup.find('h1')

    # Exibir o texto dentro da tag h1
    print(f'Titulo da Pagina:{h1.text}')

    #Exibir todos os elementos HTML correspondentes a uma tag especifica

    #Procura por todos os links na pagina
    todos_links = soup.find('a')

    #Exibir os URLs de todos os links na pagina.
    for link in todos_links:
        print(link.get('href'))

    #Acessar atributos de um elementos HTML
    img_src = soup.find('img')['src']

    print(img_src)

    #Navegar pela arvore DOM, navegar pelo HTML para encontrar elementos aninhados
    conteudo_div = soup.find('div', class_='ui-pdp-extended')
    print(conteudo_div)
    conteudo_spam = soup.find('spam', 'class_:')

    #Exibir o texto dentro da tag < div class='conteudo'>
    print('Conteudo da Div:')
    print(conteudo_div.text.strip())
    print('Preço do produto:')
    print(conteudo_spam.text.strip())

    #Encontrar todos os elementos de uma classe especifica
    todos_elementos_classe_x = soup.find_all(class_ = 'ui-pdp-extended' )

    print(todos_elementos_classe_x.text.strip())

    #Encontrar o próximo elemento irmão
    elemento_filho = title_tag.find_next_sibling()

    #Econtrar elementos pelo seletor CSS
    elemento_css = soup.select('.minha-classe_css')

else:
    print(f"A solicitação falhou com o código:")
    