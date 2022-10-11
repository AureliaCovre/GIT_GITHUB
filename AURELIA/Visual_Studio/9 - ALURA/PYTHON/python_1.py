""" PYTHON - COMEÇANDO COM A LINGUAGEM | FAZ PARTE DA FORMAÇÃO ENG.DE DADOS """

print("**********************************")
print("Bem vindo no jogo de Advinhação!")
print("**********************************")

numero_secreto = 43

chute_str = input("Digite o seu numero: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

if (numero_secreto == chute):
    print("Você Acertou")
else: 
    print("Você Errou")  

print("Fim de jogo!")     