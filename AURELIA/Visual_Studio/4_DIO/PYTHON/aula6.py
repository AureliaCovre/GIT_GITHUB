""" Objetivos da aula: 1. Aprender sobre conjuntos |2. Aprender a manipular conjuntos |3. Aplicabilidade de conjuntos;
"""

conjunto = {1,2,3,4}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print("União: {}".format(conjunto_uniao))
# conjunto.add(5) # Adicionando elemento ao conjunto
# conjunto.discard(2) #Removendo elemento do conjunto
# print(conjunto)
# print(type(conjunto))

conjunto_interseccao = conjunto.intersection(conjunto2)
print("Intersecção: {}".format(conjunto_interseccao))

conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print("Diferença entre 1 e 2: {} ".format(conjunto_diferenca))
print("Diferença entre 2 e 1: {} ".format(conjunto_diferenca2))

# DIFERENÇA SIMETRICA:
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print("Diferença simétrica: {}".format(conjunto_diff_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b) # Retorna: True, pq 1,2,3 estão dentro do conj.b  
#conjunto_subset = conjunto_b.issubset(conjunto_a) # Retorna: False 
print("A é subconjunto de B: {}".format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print("B é um superconjunto de A: {}".format(conjunto_superset))

# Uma maneira de retirar a duplicidade de uma lista: 
lista = ["cachorro", "cachorro", "gato", "gato", "elefante"]
print(lista)
conjunto_animais = set(lista) # Convertendo a lista para conjunto
print(conjunto_animais)

lista_animais = list(conjunto_animais) #Convertendo novamente para lista mas sem as duplicidades
print(lista_animais)


