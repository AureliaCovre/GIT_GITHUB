import itertools

""" WORDLIST : são arquivos contendo uma palavra por linha. São utilizados em ataques de força bruta como quebra de autenticação, pode
ser usada para testar a autenticação e confidencialidade de um sistema.
ITERTOOLS: Esta biblioteca fornece consições para iterações como permutação e combinação.
Usaremos esta biblioteca para gerar uma lista com vários caracteres diferentes e sem repetição de palavras. """

string = input("String a ser permutada: ")
resultado = itertools.permutations(string, len(string))
#resultado = itertools.permutations("abc", 3)   # Funciona sem o input

for i in resultado:
    print("".join(i))