import socket

# Criando o objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!!!")

host = "localhost"
port = 5432

s.bind((host, port))
mensagem = "\nServidor diz: Olá cliente e ai blz?"

while 1 :
    dados, end = s.recvfrom(4096)
    
    if dados:
        print("Servidor enviando msg...")
        s.sendto(dados + (mensagem.encode()), end )   