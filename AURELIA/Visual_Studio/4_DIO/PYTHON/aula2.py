a = int(input("Entre com primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
soma = a + b
subtração = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))
print("soma: " + str(soma)) #CONVERTENDO SOMA, DE INT PARA STR

print("subtração: " + str(subtração))
print("multiplicação: " + str(multiplicacao))
print(int(divisao)) #CONVERTENDO DIVISÃO, DE FLOAT PARA INT
print("Divisão: ", divisao)
print("resto: ", resto)
print("soma: {}. subtracao {}".format(soma, subtração))
print("soma: {soma}. subtracao {sub}".format(soma=soma, sub=subtração))

print("Soma: {soma}. \nSubtracao {sub} "
      "\nMultiplicação: {multiplicacao}"
      "\nDivisão: {divisao}"
      "\nResto: {resto}".format(soma=soma, 
                              sub=subtração,
                              resto=resto,
                              multiplicacao=multiplicacao,
                              divisao=divisao))



