### LAÇOS DE REPETIÇÃO ###

# # Imprimir os 100 primeiros numeros 
# for x in range (100):
#     print(x)
    
# # Imprimir de 1 a 100   
# for x in range (1,100):
#     print(x)    

# # Imprimir os numeros primos (são os numeros que apenas podem ser divididos por 1 ou por eles mesmo)
# a = int(input("Digite um número: "))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1

# if div == 2:
#     print("numero {} é primo".format(a))  
# else:
#     print("numero {} não é primo".format(a))     

# # Imprimir os numeros primos (são os numeros que apenas podem ser divididos por 1 ou por eles mesmo)
# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
    
#     if div == 2:
#         print(num)  
    
# # LAÇO DE REPETIÇÃO ATE O NUMERO 10
# a = 0
# while a < 10:
#     print(a)
#     a += 1
        
#
# nota = int(input("Entre com a nota: "))
# while nota > 10:
#     nota = int(input("Nota inválida. Entre com a nota correta: "))       

#

#
a = int(input("Primeiro bimestre: "))
while a > 10:
    a = int(input("Você digitou errado. Primeiro bimestre: "))   
b = int(input("Segundo bimestre: "))
while b > 10:
    b = int(input("Você digitou errado. Segundo bimestre: ")) 
c = int(input("Terceiro bimestre: "))
while c > 10:
    c = int(input("Você digitou errado. Terceiro bimestre: "))  
d = int(input("Quarto bimestre: "))
while d > 10:
    d = int(input("Você digitou errado. Quarto bimestre: "))   
media = (a + b + c + d) / 4
print("media: {}".format(media))    
    