## DESAFIO 003: Crie um programa que leia dois numeros e mostre a soma entre eles.

# num1 = int(input("Digite o primeiro numero: "))
# num2 = int(input("Digite o segundo numero: "))
# soma = num1 + num2
# print("O resultado da soma é: ", soma)
# #print("A soma entre {} e {} é igual a {}!".format(num1, num2, soma))

# -- ----------------------------------------
### DESAFIO 004 - Faça um programa que leia algo pelo teclado e mostre ana tela o seu
###     tipo primitivo e todas as informações possiveis sobre ela.
 
# a = input("Digite algo: ")
# print("O tipo primitivo desse valor é ", type(a)) 
# print("Só tem espaços? ", a.isspace())
# print("É um numero? ", a.isnumeric())
# print("É alfabético? ", a.isalpha())
# print("é alfanumerico? ", a.isalnum())
# print("esta em maisculas? ", a.isupper())
# print("esta em minusculo? ", a.islower())
# print("esta capitalizado? ", a.istitle()) #ex: Python, Aurélia 

# -- ----------------------------------------
### Aula 7 – Operadores Aritméticos
""" Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência
dentro de expressões matemáticas. Veja como funcionam os operadores de adição, subtração, multiplicação, 
divisão, exponenciação e quociente na linguagem Python. """

# Operadores:
#  + = Adição
#  - = Subtração
#  * = Multiplicação
# #  / = Divisão
# #  ** =  Potência 
# #  // = Divisão inteira
# #  % = Resto da divisão

# 5 + 2 == 7
# 5 - 2 == 3
# 5 * 2 == 10
# 5 / 2 == 2.5
# 5 ** 2 == 25
# 5 // 2 == 2
# 5 % 2 == 1

# Ordem de precedencia:
# 1 ()
# 2 **
# 3 *, /, //, %
# 4 + , - 

# 5 + 3 * 2 == 11 # 3*2 = 6 + 5
# 3 * 5 + 4 ** 2 == 31 # 4**2 = 16, 3*5 = 15, 15+16 = 31
# 3*(5+4)**2 == 243   #5+4 = 9, 9**2 = 81, 81*3 = 243
# pow(4,3) # É o mesmo que 4**3 (4 ao cubo)
# 81**(1/2) # Raiz quadrada de 81. Calcular a raiz quadrada de um numero é o mesmo q calcular a potencia dele por 1/2
# 127**(1/3) #para calcular a raiz cubica

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 005 - Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
# n = int(input("Digite um número: "))
# s = n + 1
# a = n - 1
# print("O número escolhido foi:", n, ". O seu sucessor é:", s, ". Seu antecessor é:", a)

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
# n = int(input("Digite um número: "))
# print("O número escolhido foi: {}, o dobro disso é {}, o triplo {}, e a raiz quadrada{}".format(n, (n*2), (n*3),(n**(1/2))))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 007 - Desenvolva um programa que leia as 2 notas de um aluno, calcule a média
# n1 = float(input("Primeira nota:"))
# n2 = float(input("Segunda nota: "))
# media = (n1 + n2) /2
# print(media)

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros   
# m = float(input("Digite os metros: "))
# c = m*100
# ml = m * 1000
# print("Metros:", m, ". Centimetros:", c, ". Milimetros:", ml)

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 009 - Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada
# n = int(input("Digite um número: "))
# a = n * 2
# b = n * 3
# c = n * 4
# d = n * 5
# e = n * 6
# f = n * 7
# g = n * 8
# h = n * 9
# i = n * 10
# print("A tabuada de", n, "é: ", n,a,b,c,d,e,f,g,h,i)
# print("-" * 12)
# print("{} x {:2} = {}".format(n,1, n*1))
# print("{} x {:2} = {}".format(n,2, n*2))
# print("{} x {:2} = {}".format(n,3, n*3))
# print("{} x {} = {}".format(n,10, n*10))
# print("-" * 12)

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 010 - Crie um programa q leia qto dinheiro uma pessoa tem e qtos dolares ela pode comprar. considere UU$1 = 3,27
# dinheiro = float(input("Digite quanto vc tem R$ "))
# dolar = dinheiro / 3.27
# print("Com R$ {:.2f} você pode comprar U$${:.2f}".format(dinheiro, dolar))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 011 - Faça um programa q leia a largura e altura de uma parede em metros, calcule a sua area e a qtd
### de tinta necessario para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m2.
# altura = float(input("Qual a altura? ")) 
# largura = float(input("Qual a largura? "))
# area = largura * altura
# tinta = area /2
# print("É necessario", tinta, "litros de tinta!")

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 012 - Faça um algoritmo q leia o preço de um produto e mostre seu novo preço, com 5% de desconto
# p = float(input("Digite o valor do produto:"))
# d = p - (p * 5 / 100)
# print("Com desconto o produto custa ", d)

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 013 - Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
# salario = float(input("Digite o salario: R$"))
# aumento = salario + (salario * 15 / 100)
# print("O salário era R${}, e com o aumento ele passou a ser R${}".format(salario, aumento))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta 
### para graus Fahrenheit.
# c = float(input("Informe a temperatura em C: "))
# f = 9 * c / 5 + 32
# print("A temperaura de {}C corresponde a {}F!".format(c,f)) 

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 015:Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e 
### a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 
### R$60 por dia e R$0,15 por Km rodado.
# dias = int(input("Quantos dias alugados?"))
# km = float(input("qtos km rodados?"))
# pago = (dias * 60) + (km * 0.15)
# print("o total a pagar é de R${:.2f}".format(pago))

#-- ------------------------------------------------------------------------------------------------------------
from calendar import c
import math

### DESAFIO 016: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela 
# a sua porção inteira. Ex: Digite 6.127. O número 6.127 tem a parte inteira 6.

# num = float(input("Digite um número:"))
# inteiro = math.trunc(num) #Retorna o Realvalor x truncado para an Integral(geralmente um inteiro). Delegados a x.__trunc__().
# print("O número digitado foi {}, e tem a sua parte inteira {}.".format(num, inteiro))
# print("O número digitado foi {}, e tem a sua parte inteira {}.".format(num, int(num)))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retangulo, calcule e mostre o comprimento da hipotenusa.

# co = float(input("Comprimento do cateto oposto: "))
# ca = float(input("Comprimento do cateto adjacente: "))
# # hi = (co ** 2 + ca ** 2) ** (1/2)
# # print("A hipotenusa mede {:.2f}".format(hi))
# ## 2 opção com a biblioteca math:
# hi = math.hypot(co, ca)
# print("A hipotenusa mede {:.2f}".format(hi))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
# e tangente desse ângulo.

# an = float(input("Digite o ângulo que você deseja: "))
# seno = math.sin(math.radians(an))
# print("O ângulo de {} tem o SENO de{:.2f}".format(an, seno))
# cosseno = math.cos(math.radians(an))
# print("O ângulo de {} tem o COSSENO de {:.2f}".format(an, cosseno))
# tangente = math.tan(math.radians(an))
# print("O ângulo de {} tem a TANGENTE  de {:.2f}".format(an, tangente))

# # 2 opção:
# from math import radians, sin, cos , tan
# an = float(input("Digite o ângulo que você deseja: "))
# seno = sin(radians(an))
# print("O ângulo de {} tem o SENO de{:.2f}".format(an, seno))
# cosseno = cos(radians(an))
# print("O ângulo de {} tem o COSSENO de {:.2f}".format(an, cosseno))
# tangente = tan(radians(an))
# print("O ângulo de {} tem a TANGENTE  de {:.2f}".format(an, tangente))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# import random
# n1 = str(input("Primeiro aluno: "))
# n2 = str(input("Segundo aluno: "))
# n3 = str(input("Terceiro aluno: "))
# n4 = str(input("Quarto aluno: "))
# lista = [n1, n2, n3, n4]
# escolhido = random.choice(lista)
# print("O aluno escolhido foi {}".format(escolhido))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos 
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# import random
# n1 = str(input("Primeiro aluno: "))
# n2 = str(input("Segundo aluno: "))
# n3 = str(input("Terceiro aluno: "))
# n4 = str(input("Quarto aluno: "))
# lista = [n1, n2, n3, n4]
# random.shuffle(lista) # Embaralha a lista
# print("A ordem de apresentação será: ")
# print(lista)

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
""" salvar o arquivo mp3 na mesma pasta do cod (igual ao csv)"""
# import pygame
# pygame.init()
# pygame.mixer.music.load("nome_arquivo")
# pygame.mixer.music.play()
# pygame.event.wait()

#-- ------------------------------------------------------------------------------------------------------------
"""     AULA 9 - Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos 
aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), 
upper(), lower(), capitalize(), title(), strip(), junção com join().  """

# -- EXEMPLOS DE FATIAMENTO

# frase = "Curso em video Python"

# # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# # C U R S O   E M   V  I  D  E  O     P  Y  T  H  O  N

# frase[9] # Imprime apenas o caractere 9 ou seja a letra V
# frase[9:13] # Imprime do 9 até o 12: VIDE
# frase[9:21] # Imprime do 9 até o 20: VIDEO PYTHON
# frase[9:21:2] #Aqui ele pula de 2 em 2, do 9 ao 20 : VDOPTO
# frase[:5] # Quando omito de onde ele começa, ele começa no inicio, ou seja imprime do 0 ao 4: CURSO
# frase[15:] # Indicou de onde quer começar, dai ele imprime até o final: PYTHON
# frase[9::3] # Indica que começa no 9 até o final, contando de 3 em 3: VEPH

# ### -- ANÁLISE DE STRING
# len(frase)  # Mostra o comprimento da frase
# frase.count("o")    # Conta qtas vezes a letra "o" aparece.
# frase.count("o", 0, 13)     # Considera do 0 ao 13 e conta qtos "o" aparece.*lembrando que o ultimo(13) é desconsiderado 
# frase.find("deo")   # Encontra que posição começa, nesse ex é a posição 11
# frase.find("Android")   # Como não existe, ele retorna -1
# "curso" in frase    # O operador in, vai responder true ou false


# ### -- TRANSFORMAÇÃO DE STRING
# frase.replace("PYTHON", "ANDROID") # Substitui de forma secundaria, o python pelo android
# frase.upper() # Metodo que transforma tudo em maiusculo
# frase.lower() # Deixa tudo minusculo
# frase.capitalize() # Deixa o primeiro caractere maiusculo e o restante em minusculo
# frase.title() # Analisa qtas palavras tem na string e transforma a primeira letra de cada frase em maiusculo

# # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 
# #       A P R E N D A     P  Y  T  H  O  N
# frase.strip() # Remove os espaços do começo e do fim.
# frase.rstrip() # Remove apenas os ultimos espaços.
# frase.lstrip() # Remove os espaços do começo.


# ### -- DIVISÃO DE STRING
# frase.split() # Refaz uma indexação nova: 
# # 0 1 2 3 4   0 1   0 1 2 3 4   0 1 2 3 4 5 
# # C U R S O   E M   V I D E O   P Y T H O N

# ### -- JUNÇÃO DE STRING
# "-".join(frase) # Ele junta varias str em apenas uma, ex: curso-em-video-python

# AULA 9 - TESTES
# frase = "Curso em video Python"
# print(frase[1:15:2])
# print(frase.upper().count("0"))
# print(len(frase))
# print(frase.replace("Python", "android"))
# print("Curso" in frase)

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
### A. Nome com todas as letras maisculas;
### B. Nome com todas as letras minusculas;
### C. Quantas letras ao todo, sem contar espaços;
### D. Quantas letras tem o primeiro nome;

# nome = str(input("Digite seu nome completo: ")).strip() #eliminando os espaços antes e depois
# print("Aqui esta a analise de seu nome... ")
# print("A. Nome maisculo: {}".format(nome.upper()))
# print("B. Nome minusculo: ",nome.lower())
# print("C. O seu nome tem {} letras".format(len(nome) - nome.count(" ")))
# #print("D. Quantas letras tem o primeiro nome: {} ".format(nome.find(" ")))
# separa = nome.split()
# print("O seu primeiro nome é {} e ele tem {} letras". format(separa[0], len(separa[0])))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
### Ex : numero digitado: 1834 | imprime unidade: 4 / dezenas: 3 / centena: 8 / milhar: 1

# numero = int(input("Digite um numero: "))
# n = str(numero)
# print("Analisando seu número....")
# print("Unidade: {}".format(n[3]))
# print("Dezena: {}".format(n[2]))
# print("Centena: {}".format(n[1]))
# print("Milhar: {}".format(n[0]))

# numero = int(input("Digite um numero: "))
# u = numero // 1 % 10
# d = numero // 10 % 10
# c = numero // 100 % 10
# m = numero // 1000 % 10
# print("Unidade: {}".format(u))
# print("Dezena: {}".format(d))
# print("Centena: {}".format(c))
# print("Milhar: {}".format(m))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
# cidade = str(input("Digite o nome da cidade: ")).strip() # STRIP para tirar os espaços antes e depois
# print(cidade[:5].upper == "SANTO") #Com o upper antes de analisar ele deixa tudo maiusculo, assim independente do 
#                                       #que for digitado ele analisa corretamente.


#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
# nome = str(input("Digite seu nome: ")).strip()
# print("Seu nome tem Silva? {}".format("silva" in nome.lower()))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 026 - Faça um programa que leia uma frase pelo teclado e mostre:
### A. Quantas vezes aparece a letra "A".
### B. Em que posição ela aparece pela primeira vez.
### C. Em que posição ela aparece pela ultima vez.
# frase = str(input("Digite uma frase: ")).strip().upper()
# print("A. Quantas vezes aparece a letra A: ", frase.count("A"))
# print("B. Em que posição ela aparece pela primeira vez:  ", frase.find("A")+1)
# print("C. Em que posição ela aparece pela ultima vez.: ", frase.rfind("A")+1)


#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o 
# # último nome separadamente. EX: Ana Maria de Souza | Primeiro: Ana / Último: Souza

# nome = str(input("Digite seu nome: ")).strip()
# n = nome.split() # o split separa as palavras por espaços e joga em uma lista
# #print("o que o split faz: ", n)
# print("Primeiro nome: {}".format(n[0]))
# print("Ultimo nome: {}".format(n[len(n)-1])) #Aqui ele colocou len para ler inteiro e -1 pra pegar o primeiro de tras pra frente.
#                                              #Sem o len tbm funcionou

#-- ------------------------------------------------------------------------------------------------------------
"""     AULA 10 - Nessa aula, vamos aprender com utilizar estruturas condicionais simples e compostas nos seus 
programas em Python. """

# tempo = int(input('Quantos anos tem seu carro? '))
# if tempo <= 3:
#     print("Seu carro é novo!")
# else:
#     print("Seu carro esta velhinho!")   
# print("--FIM--")  

# # Condição simplificada:
# tempo = int(input("Quantos anos tem seu carro? "))
# print("carro novo" if tempo <=3 else "carro velho" )   
# print("--Fim--")
#-- ------------------------------------------------------------------------------------------------------------

# nome = str(input("Qual seu nome? "))
# if nome == "Gustavo":
#     print("Que nome lindo ")
# print("Bom dia, {}".format(nome))    


# -- -----------------
# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# m = (n1 + n2) / 2
# print("A sua média foi{:.1f}".format(m))
# # if m >= 6.0:
# #     print("Sua média foi boa! PARABÉNS!")
# # else: 
# #     print("Sua média foi ruim! ESTUDE MAIS!")
# print("PARABÉNS!" if m >=6 else "ESTUDE MAIS!")    # CONDIÇÃO SIMPLIFICADA

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para 
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa devera escrever na tela se o 
# usuário venceu ou perdeu.

# from random import randint
# from time import sleep
# computador = randint(0,5) # Faz o computador "pensar" / faz o sorteio
# print("-=-"*10)
# print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
# print("-=-"*20)
# jogador = int(input("Em que número eu pensei? "))
# print(" PROCESSANDO ... ")
# sleep(2)
# if jogador == computador:
#     print("Você ganhou!")
# else:
#     print("Ganhei! Pensei no número {} e não {}".format(computador, jogador))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma 
# mensagem dizendo que ele foi multado.  A multa vai custar R$ 7,00 por cada km acima do limite.

# velocidade = float(input("Qual a velocidade atual? "))
# if velocidade > 80:
#     multa = (velocidade - 80) * 7
#     print("Você ultrapassou o limite de velocidade permitido. MULTA DE R${}".format(multa))
# else:
#     print("Você esta dentro do limite permitido!")    
    
#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

# n = int(input("Digite um numero: "))
# resultado = n % 2 
# if resultado == 0:
#     print("{} é um numero par!".format(n))
# else:
#     print("{} é um numero ímpar! ".format(n))    

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 031 - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem 
# cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

# distancia = float(input("Qual a distancia da viagem em km? "))
# if distancia <= 200:
#     print("O valor da corrida é : ", distancia * 0.50)
# else: 
#    print("O valor da corrida é : ", distancia * 0.45)     
    

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 032 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# from datetime import date 
# ano = int(input("Que ano deseja analisar? Ou digite 0 para analisar o ano atual. "))
# if ano == 0:
#     ano = date.today().year # Aqui pega o ano configurado na maquina
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
#     print("o ano {} é BISSEXTO!".format(ano))
# else:
#     print("o ano {} NÂO é BISSEXTO!".format(ano))


#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# a = int(input("Digite o primeiro valor: "))
# b = int(input("Digite o segundo valor: "))
# c = int(input("Digite o terceiro valor: "))
# menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c  
# maior = a
# if b > a and b > c:
#    maior = b
# if c > a and c > b:
#     maior = c    
# print("O menor valor é {}".format(menor))      
# print("O maior valor é {}".format(maior))    


#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 034 - Escreva um programa que pergunte qual o salário de um funcionário e calcule o valor do seu aumento.
# Para salário superior a R$ 1.250,00 calcule um aumento de 10%. Para inferiores ou iguais, aumento de 15%.

# salario = float(input("Qual seu salario? "))
# if salario < 1250:
#     print("Você recebera um aumento de 10%: ", salario * 0.10)
# else:
#     print(" O seu aumento será de 15%: ", salario * 0.15)   
    
# #Guanabara:
# salario = float(input("Qual salario do funcionario? "))
# if salario < 1250:
#     novo = salario + (salario * 15 / 100)
# else:
#     novo = salario +(salario * 10 / 100)
# print(" Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.".format(salario, novo))       

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.

# r1 = int(input("Digite a primero segmento: "))
# r2 = int(input("Digite a segundo segmento: "))
# r3 = int(input("Digite a terceiro segmento: "))

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print("Os segmentos acima PODEM FORMAR UM TRIANGULO") #sem cor
#     print("Os segmentos acima \033[32mPODEM FORMAR UM TRIANGULO")
# else:
#     print("Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO")  #sem cor
#     print("Os segmentos acima \033[31mNÃO PODEM FORMAR UM TRIANGULO")    0

#-- ------------------------------------------------------------------------------------------------------------
"""     AULA 11 - ADICIONANDO CORES NO PYTHON    """

#Codigo ANSI:
#\033["estilo; cor_texto;cor_fundo"m 
# exemplo: \033[0;33;44m

''' ESTILO (STYLE):
0 - None
1 - Bold
4 - Underline
7 - negative'''

""" TEXTO (TEXT):
30 - branco
31 - vermeho
32 - verde
33 - amarelo 
34 - azul
35 - rosa
36 - turquesa
37 - cinza"""

""" cor de fundo (BACK):
40 - branco
41 - vermeho
42 - verde
43 - amarelo 
44 - azul
45 - rosa
46 - turquesa
47 - cinza"""

# print("\033[1;31;43mOlá, Mundo!\033[m")
# print("\033[4;30;45mOlá, Mundo!\033[m")

# #-- ----------
# a = 3
# b = 5
# print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!".format(a,b))

# # -- ----------
# nome = "Guanabara"
# print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format("\033[4;34m", nome, "\033[m"))

# # -- ----------
# nome = "Guanabara"
# cores = {"limpa":"\033[m",
#         "azul":"\033[34m",
#         "amarelo":"\033[33m",
#         "pretoebranco":"\033[7;30"}
# print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format(cores["amarelo"], nome, cores["limpa"]))










 








