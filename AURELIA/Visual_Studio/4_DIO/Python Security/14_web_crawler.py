"""
WEB CRAWLER: é uma ferramenta usada para encontrar, ler e indexar páginas de um site. É como um robô que captura 
informações de cada um dos links que encontra pela frente, cadastra e compreende o que é mais relevante. (palavras-chaves)
Muito utilizado em levantamento de informações em um processo de pentest.

--- BIBLIOTECAS:
- BEAUTFULSOUP: É uma biblioteca de extração de dados de arquicos HTML e XML.
- OPERATOR: Exporta um conjunto de funções eficientes correspondentes aos operadores intrínsecos do Python como:+-*/not and
- COLLECTIONS: Nos ajuda a preencher e manipular eficientemente as estruturas de dados como tuplas, dicionários e listas.
"""

import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url): # função que starta a url
    wordlist = [] # lista vazia que vai armazenar o conteudo do site 
    source_code = requests.get(url).text
    
    soup = BeautifulSoup(source_code, "html.parser") #Faz a requisição dos dados da url que será passada e vai transformar em html
    
    # Text in given web-page is stored under
    # The <div> tags with class <entry_content>
    for each_text in soup.findAll("div", {"class": "entry_content"}): # vai procurar tudo q existe com div e class
        content = each_text.text  #transforma o conteudo html em texto (string)
                   
        words = content.lower().split() # Transforma a string em letras minusculas e split, ou seja cada conteudo 1 linha
        
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)
        

def clean_wordlist(wordlist): # Essa função remove qualquer simbolo indesejado
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%¨&*()_+={[}]|\;:.><,?/-/"
        
        for i in range(0, len(symbols)): #percorre a wordlist e faz um replace dos simbolos por nada
            word = word.replac(symbols[i],'')

        if len(word) > 0: #Aqui ele faz que se word for maior que 0, ele limpa a lista
            clean_list.append(word)
    create_dictionary(clean_list)
    

def create_dictionary(clean_list): # cria o dicionario, contendo cada palavra e faz uma contagem 
    word_count = {}
    
    for word in clean_list: # Exibe a contagem e faz um top 20 de palavras mais utilizadas
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        
    # Mostra as palavras chaves com mais ocorrencias nesse site        
    for key, value in sorted(word_count.items(), 
                            key = operator.itemgetter(1)):    
        print("% s: % s " %(key, value))
        
    c = Counter(word_count) 
    
    top = c.most_common(10)
    print(top)
    
if __name__ =="__main__":
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
    
                   
                
            


    
            
            
    
