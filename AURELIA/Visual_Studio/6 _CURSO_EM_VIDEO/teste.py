segundos = int(input())

# para cada 60 segundo == 1 minutos
# para cada 60 minutos == 1 hora



horas = int(segundos / 3600)
print(horas)
resto = int(horas % 3600 >0)
print(resto)

# minutos = int(segundos * 60) #TODO Implementar a formula para calcular os minutos.
# horas = int( minutos * (segundos * 60)#TODO Implementar a formula para calcular as horas.
# minutos = int(minutos - (horas * 60))

# print("{}:{}:{}".format(horas, minutos, segundos))