import os #Importando a biblioteca os que vai trazer todas as depencias do sistema operacional
import time # Importamos a biblioteca time para trabalhar com tempo de execução


# Com a abertura do host.txt como arquivo, criamos uma variavel chamada dump e pedimos para ler o arquivo
# e jogar dentro de dump. Já no splitlines esta colocando em linhas separadas.
with open("host.txt") as file:  
    dump = file.read()
    dump = dump.splitlines()
    
    # Para cada ip em dump, vamos imprimir o verificando ip / Na linha 16: ele vai jogar um comando (ping -n 2)
    # para enviar 2 pacotes.    
    for ip in dump:
        #print("ping" + ip)   
        print("Verificando o IP", ip)
        print("-" * 60)
        os.system("ping -n 2 {}".format(ip)) 
        print("-" * 60)
        time.sleep(5) # Espera de 5 segundos na execução de um comando para o outro.