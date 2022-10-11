"""     AULA 12 - CONDIÇÕES ANINHADAS (Aninhadas = porque uma esta dentro da outra)
Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif..else 
em programas Python  """

# nome = str(input("Qual é seu nome? "))
# if nome == "Gustavo":
#     print("Que nome bonito!")
# elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
#     print("Seu nome é bem popular no Brasil!")  
# elif nome in " Ana Claudia Jessica Juliana": # Se o nome estiver aqui dentro
#     print("Belo nome feminino")     
# else:
#     print("Seu nome é normal")    
# print("tenha um bom dia {}".format(nome))

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 036 - Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa. O programa vai 
# perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode
# exceder 30% do salário ou então o empréstimo será negado.

# casa = float(input("Qual o valor da casa? "))
# salario = float(input("Qual o salario? "))
# anos = int(input("Em quantos anos você vai pagar? "))
# prestacao = casa / (anos * 12)

# print("=*" *30)
# print( "=== ANALISE DE EMPRESTIMO ===")
# print("Para a compra de uma casa no valor de R$ {:.2f}, com salario de R$ {:.2f} e pagamento em {} anos, a parcela seria no valor de R$ {:.2f}".format(casa, salario, anos,prestacao))
# percentual = salario * 30 / 100
# if prestacao > percentual:
#     print("Emprestimo NEGADO, a parcela de R$ {:.2F} ficou maior que os 30% do salario R$ {:.2F}".format(prestacao, percentual))
# else:
#     print("Parabens seu emprestimo foi APROVADO! Sua parcela mensal será de R$ {:.2F}".format(prestacao)) 
    
#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 037 - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# n = int(input("Digite um numero inteiro: "))
# print("""Escolha a opção: 
#       1 - converter para Binário
#       2 - converter para OCTAL
#       3 - converter para HEXADECIMAL""")
# opcao = (int(input("Sua opção: ")))

# if opcao == 1:
#     print("{} convertido para BINÁRIO é igual a {}". format(n, bin(n)[2:]))
# elif opcao == 2:
#     print("{} convertido para OCTAL é igual a {}".format(n, oct(n)[2:]))
# elif opcao == 3:
#     print("{} convertido para HEXADECIMAL é igual a {}".format(n, hex(n)[2:]))
# else:
#     print("Opção invalida! Tente novamente!")            
    
# """ P.S.: em todos primeiro aparece o 0b para Binario , 0o para Octal e 0x para Hexadecimal, por isso colocamos o 
# [2:] ao final , assim ele printa apenas o numero que interessa """


#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 038 - Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

# n1 = int(input("Digite o primeiro valor: "))
# n2 = int(input("Digite o segundo valor: "))

# if n1 == n2:
#     print("Não existe valor maior, os dois são iguais")
# elif n1 > n2:
#     print(" O primeiro valor é maior")
# else:
#     print("O segundo valor é maior")
        

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do 
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# from datetime import date

# ano = int(input("Ano de nascimento: "))
# data = date.today().year
# #ano_atual = data.year
# idade = (data - ano)

# print("Quem nasceu em {}, tem {} anos em {}".format(ano, idade, data))

# if idade > 18:
#     dif = idade - 18
#     print("Você ja deveria ter se alistado há {} anos".format(dif))
#     alistamento = data - dif
#     print("Seu alistamento foi em {}.".format(alistamento))            
# elif idade < 18:
#     dif = (18 - idade)
#     print("Daqui a {} anos você deve se alistar ao serviço militar.".format(dif))  
#     dif = data + dif
#     print("Seu alistamento será em {}.".format(dif))
# else:
#     print("Em {} você completa 18 anos, deve se alistar IMEDIATAMENTE ao serviço militar.".format(data))  
    
# # Solução Guanabara:  
# atual = date.today().year
# nasc = int(input("Ano nascimento: "))
# idade = atual - nasc
# print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
# if idade == 18:
#     print("Você tem que se alistar IMEDIATAMENTE!")
# elif idade < 18:
#     saldo = 18 - idade
#     print("Ainda faltam {} anos para o alistameento.".format(saldo))
#     ano = atual + saldo
#     print("Seu alistamento será em {}.".format(ano))
# elif idade >18:
#     saldo = idade -18
#     print("Você já deveria ter se alistado há {} anos.".format(saldo))
#     ano = atual - saldo
#     print("Seu alistamento foi em {}.".format(ano))            
 

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO 
   
# n1 = float(input("Primeira nota: "))
# n2 = float(input("Segunda nota: "))
# media = (n1 + n2) / 2

# if media < 5:
#     print("Quem tirou {} e {} tem a média de {}, aluno REPROVADO.".format(n1, n2, media))
# elif media > 7:
#     print("Quem tirou {} e {} tem a média de {}, aluno APROVADO.".format(n1, n2, media))
# else:
#     print("Quem tirou {} e {} tem a média de {}, aluno em RECUPERAÇÃO".format(n1, n2, media))        
  
# # # Solução Guanabara:  
# n1 = float(input("Primeira nota: "))
# n2 = float(input("Segunda nota: "))
# media = (n1 + n2) / 2
# print("Tirando{:.1f} e {:.1f}, a média do aluno é {:.1f}".format(n1, n2, media))
# if 7 > media >= 5:
#     print("O aluno está em RECUPERAÇÃO.")
# elif media < 5:
#     print("O aluno está em REPROVADO.")
# elif media >= 7:
#     print("O aluno está APROVADO.")        
    
#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um 
# atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

# from datetime import date
# atual = date.today().year
# nasc = int(input("Ano de nascimento: "))
# idade = atual - nasc
# if idade <=9:
#     print("Em {} o atleta nascido em {}, tem {} anos. Ele esta na categoria MIRIM.".format(atual, nasc, idade))
# elif 9 < idade <=14:
#     print("Em {} o atleta nascido em {}, tem {} anos. Ele esta na categoria INFANTIL.".format(atual, nasc, idade))
# elif 14 < idade <= 19:
#     print("Em {} o atleta nascido em {}, tem {} anos. Ele esta na categoria JUNIOR.".format(atual, nasc, idade))
# elif 19 < idade <= 25:
#     print("Em {} o atleta nascido em {}, tem {} anos. Ele esta na categoria SÊNIOR.".format(atual, nasc, idade))   
# else:
#     print("Em {} o atleta nascido em {}, tem {} anos. Ele esta na categoria MASTER.".format(atual, nasc, idade))     

# ### Solução Guanabara:  
# from datetime import date
# atual = date.today().year
# nasc = int(input("Ano de nascimento: "))
# idade = atual - nasc
# print(" O atleta tem {} anos.".format(idade))
# if idade <=9:
#     print("Classificação: MIRIM.")
# elif idade <=14:
#     print("Classificação: INFANTIL.")
# elif idade <= 19:
#     print("Classificação: JUNIOR.")
# elif idade <= 25:
#     print("Classificação: SÊNIOR.")  
# else:
#     print("Classificação: MASTER.")     

#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 042 - Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo 
# será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

# r1 = int(input("Digite a primero segmento: "))
# r2 = int(input("Digite a segundo segmento: "))
# r3 = int(input("Digite a terceiro segmento: "))

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print("Os segmentos acima PODEM FORMAR UM TRIANGULO") #sem cor
#     print("Os segmentos acima \033[32mPODEM FORMAR UM TRIANGULO")
#     if r1 == r2 and r1 == r3:
#         print("O triângulo é do tipo EQUILÁTERO que tem todos os lados iguais")
#     elif r1 == r2 or r1 == r3 or r2 == r3:
#         print("O triângulo é do tipo ISÓSCELES que tem dois lados iguais")
#     else:
#         print("O triângulo é do tipo ESCALENO que tem todos os lados DIFERENTES")
# else:
#     print("Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO")  #sem cor
#     print("Os segmentos acima \033[31mNÃO PODEM FORMAR UM TRIANGULO")
    
### SOLUÇÃO GUANABARA:

# r1 = int(input("Digite a primero segmento: "))
# r2 = int(input("Digite a segundo segmento: "))
# r3 = int(input("Digite a terceiro segmento: "))

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print("Os segmentos acima PODEM FORMAR UM TRIANGULO ", end="") 
#     if r1 == r2 == r3:
#         print("EQUILÁTERO")
#     elif r1 != r2 != r3 != r1:
#         print(" ESCALENO ")
#     else:
#         print("ISÓSCELES")
# else:
#     print("Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO") 
        
#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa 
# Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

# peso = float(input(" Seu peso: "))
# altura = float(input(" Sua altura: "))
# imc = peso / (altura ** 2)
# if imc < 18.5:
#     print("Seu IMC é {:.2f}, status ABAIXO DO PESO.".format(imc)) 
# elif imc < 25:
#     print("Seu IMC é {:.2f}, status PESO IDEAL.".format(imc)) 
# elif imc <30:
#     print("Seu IMC é {:.2f}, status SOBREPESO.".format(imc))    
# elif imc <40:
#     print("Seu IMC é {:.2f}, status OBESIDADE.".format(imc))     
# else:
#     print("Seu IMC é {:.2f}, status OBESIDADE MORBIDA.".format(imc))     
    
#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

# produto = float(input("Valor do produto: R$ "))
# print("""Selecione a forma de pagamento:
#       1 - Dinheiro
#       2 - Cheque à vista
#       3 - Cartão debito 
#       4 - Cartão crédito (até 2x)
#       5 - Cartão de crédito (3x ou mais)  """)
# opcao = int(input("Forma de pagamento: "))

# if opcao == 1:
#     print("O valor do produto era de {:.2f}, mas como a forma de pgto será em Dinheiro, você receberá 10% de desconto e pagara apenas: R$ ".format(produto), end="")
#     print(produto - ((produto * 10) /100))
# elif opcao == 2:
#     print("O valor do produto era de {:.2f}, mas como a forma de pgto será em Cheque a vista, você receberá 10% de desconto e pagara apenas: R$ ".format(produto), end="")
#     print(produto - ((produto * 10) /100))
# elif opcao == 3:
#     print("O valor do produto era de {:.2f}, mas como a forma de pgto será no cartão de debito, você receberá 5% de desconto e pagara apenas: R$ ".format(produto), end="")
#     print(produto - ((produto * 5) /100))  
# elif opcao == 4:
#     print("O valor do produto era de {:.2f}, mas como a forma de pgto será no cartão de credito em 2x, o preço é normal: R$ ".format(produto), end="")
#     print(produto)
# elif opcao == 5:
#     print("O valor do produto era de {:.2f}, mas como a forma de pgto será no cartão de crédito em mais de 3x, você pagará um juros de 20% a mais: R$ ".format(produto), end="")
#     print(produto + ((produto * 20) /100))          
# else:
#     print("Opção invalida")

### SOLUÇÃO GUANABARA:
# print('{:=^40}'.format(" LOJAS GUANABARA "))
# preco = float(input("Preço das compras: R$ "))
# print(""" FORMAS DE PAGAMENTO:
#     1 - à vista Dinheiro / Cheque
#     2 - à vista cartão
#     3 - 2x no Cartão  
#     4 - 3x ou mais no Cartão """)
# opcao = int(input("Qual a opção? "))

# if opcao == 1:
#     total = preco - ((preco * 10) /100)
# elif opcao == 2:
#     total = preco - ((preco * 5) /100)
# elif opcao == 3:
#     total = preco - ((preco * 5) /100)
#     parcela = total / 2
#     print("Sua compra será parcelada em 2x de R$ {:.2f}".format(parcela))
# elif opcao == 4:
#    total = (preco + ((preco * 20) /100))  
#    totparc = int(input("Quantas parcelas? "))
#    parcela = total / totparc    
#    print("Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS".format(totparc, parcela))        
# else:
#     print("Opção invalida")
# print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, total))

   
#-- ------------------------------------------------------------------------------------------------------------
### DESAFIO 045 -  Crie um programa que faça o computador jogar Jokenpô com você.  
# from random import randint
# from time import sleep

# itens = ("Pedra", "Papel", "Tesoura")
# computador = randint(0,2)
# print('{:=^40}'.format(" JOKENPÔ "))
# print(""" Opções:
#     1 - PEDRA
#     2 - PAPEL 
#     3 - TESOURA""")
# jogador = int(input("Qual a sua jogada? "))

# print("JO")
# sleep(1)
# print("KEN")
# sleep(1)
# print("PÔ")

# print("-=" * 11)
# print(" Computador jogou {}".format(itens[computador]))
# print(" Jogador jogou {}".format(itens[jogador]))
# print("-=" * 11)

# if computador == 0: # o computador jogou PEDRA
#     if jogador == 0:
#         print("EMPATE")
#     elif jogador == 1:
#         print(" JOGADOR VENCEU! ")
#     elif jogador == 2:
#         print(" COMPUTADOR VENCEU! ")
#     else:
#         print("JOGADA INVALIDA!")            
# elif computador == 1: # o computador jogou PAPEL
#     if jogador == 0:
#         print("COMPUTADOR VENCEU!")
#     elif jogador == 1:
#         print(" EMPATE ")
#     elif jogador == 2:
#         print(" JOGADOR VENCEU! ")
#     else:
#         print("JOGADA INVALIDA!")  
# elif computador == 2: # o computador jogou TESOURA
#     if jogador == 0:
#         print("JOGADOR VENCEU!")
#     elif jogador == 1:
#         print(" COMPUTADOR VENCEU ")
#     elif jogador == 2:
#         print(" EMPATE ")
#     else:
#         print("JOGADA INVALIDA!") 
# else:
#     print("Opção invalida, tente novamente!")    


            