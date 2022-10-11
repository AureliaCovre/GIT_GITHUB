""" OBJETIVO DA AULA: 1. Aprender a utilizar e interagir com módulos;
                      2. Entender a importância de se utilizar módulos;
                      3. Aprender sobre funções anônimas.  """
                      
def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade= len(x)
        contador.append(quantidade)
    return contador

if __name__ == "__main__":
    lista = ["cachorro", "gato"]
    print(contador_letras(lista))    
                      