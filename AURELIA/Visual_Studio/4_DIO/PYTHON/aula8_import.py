""" OBJETIVO DA AULA: 1. Aprender a utilizar e interagir com módulos;
                      2. Entender a importância de se utilizar módulos;
                      3. Aprender sobre funções anônimas.  """
                      
from numpy import logical_and
from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ =="__main__":
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5,10)
    print(calculadora.soma())
    lista = ["cachorro", "gato", "elefante"]
    total_letras = contador_letras(lista)
    print("total de letras por palavras de lista: {}".format(total_letras))
    
    
                      