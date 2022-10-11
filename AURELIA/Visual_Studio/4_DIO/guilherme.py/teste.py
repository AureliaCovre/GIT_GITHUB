# REVISÃO 

# temperatura = int(input("Qual a temperatura: "))
temperatura = int(input('Qual a temperatura? '))
if temperatura <= 15:
  print('Está muito frio')
elif temperatura >= 50:
  print('deixamos de existir')
else:
  print('está ok')

# LISTA
carros = ["Ferrari", "Camaro", "Uno"]
print(carros[2])

# dict
obj = {'a':'computador', 'b': 'colher'}
obj['b']

# Redis


#for
for carro in carros:
    print(carro)

#import e while    
from time import sleep
tempo = 5    
while tempo > 0:
    print(tempo)
    sleep(1)
    tempo -= 1
    
#função
def quadrado(numero):
    return numero * numero

print(quadrado(3))

# função criar carro
def criar_carro(nome, cor, valor):
    return {
        "nome": nome,
        "cor": cor,
        "valor": valor
    }
    
dkv = criar_carro("DKV", "Azul", "60000")
print(dkv)
print(dkv["valor"])

def atualiza_valor(carro, novo_valor):
    carro["valor"] = novo_valor
atualiza_valor(dkv, 80000)
print(dkv["valor"])  

# Com classe

class Carro:
    def __init__(self, nome, cor, valor):
        self.nome = nome
        self.cor = cor
        self.valor = valor
        
    def atualizar_valor_do_carro(self, novo_valor):
        # if 
        self.valor = novo_valor    

uno = Carro("Uno", "Branco", "30000")
onix = Carro("Onix", "Prata", "50000")        

print(uno.nome)
print(onix.valor)

print(uno)
print(onix)

onix.atualizar_valor_do_carro(-10000)
print(onix.valor)

onix.valor
          

   