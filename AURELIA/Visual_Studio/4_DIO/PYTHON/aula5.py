### ORGANIZANDO LISTAS E TUPLAS ###

lista = [1, 10, 5, 7]
lista_animal = ["cachorro", "gato", "elefante", "Arara"]
print(lista)
print(lista_animal[1])
# Multiplicando uma lista:
nova_lista = lista_animal * 3
print(nova_lista)

soma = 0
for x in lista:
    print(x)
    soma += x   # soma todos os numeros dentro da lista
print("soma: ", soma)    

#Para fazer apenas uma soma
print(sum(lista))

# Maior valor da lista | Vale tambem para str 
print(max(lista))

# Para pesquisar se existe algo na lista
if "lobo" in lista_animal:
    print("Existe um lobo na lista")
else: 
    print("Não existe lobo na lista")   
    lista_animal.append("lobo") # Incluindo um animal á lista
    print(lista_animal) 
    
# Retirando um item da lista
lista_animal.pop()
print(lista_animal)    
    
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal) 
lista_animal.reverse() #Ordenando de tras para frente
print(lista_animal)  

# =-=-=-=-=-=-= TUPLAS =-=-=-=-=-=-=-=-=
tupla = (1,10,12,14)
print(tupla)
print(len(tupla)) #contador
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)