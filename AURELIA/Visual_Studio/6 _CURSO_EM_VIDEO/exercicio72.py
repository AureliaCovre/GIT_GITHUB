''' Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
            'dez', 'onze','doze', 'treze', 'quatrorze', 'quinze')
(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

while True:
    num = int(input('Digite um número entre 0 e 15: '))
    if 0 <= num <= 15:
        break
    print('Tente novamente. ', end= '')
print(f'Você digitou o número {cont[]}')    