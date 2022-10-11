""" WEB SCRAPING: Um web scraper é uma ferramenta de coleta de dados web, uma forma de mineração que permite a 
extração de dados de sites da web convertendo-os em informações estruturada para posterior análise.

BEAUTIFULSOUP: É uma biblioteca de extração de dados de arquicos HTML e XML.

REQUESTS: É uma biblioteca permite que vc envie solicitações HTTP em Python."""

from bs4 import BeautifulSoup
import requests

# variavel esta recebendo todo o conteudo da requisição http do site....
site = requests.get("https://www.climatempo.com.br/").content 

# objeto soup baixando do site o html
soup = BeautifulSoup(site, "html.parser")

#transforma html em string e o print vai exibir o html
# print(soup.prettify())

# temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
# print(temperatura.string)

print(soup.a)


