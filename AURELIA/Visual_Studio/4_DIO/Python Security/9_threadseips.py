from threading import Thread
import time

# Criando a função carro1 e pra essa função será passado o argumento velocidade
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        time.sleep(0.5)
        print("Piloto: {}, KM: {} \n".format(piloto,trajeto))
        
t_carro1 = Thread(target=carro, args=[1, "Bruno"])
t_carro2 = Thread(target=carro, args=[1.5, "João"])

t_carro1.start()
t_carro2.start()
        