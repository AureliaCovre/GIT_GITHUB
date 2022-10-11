import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

# Criamos a variavel hash1, onde ela recebe o contrutor "new" da biblioteca hashlib. Este construtor recebe uma str que
# diz qual o algoritmo de hash que vamos utilizar 
hash1 = hashlib.new("ripemd160")
# Aqui estamos dizendo ao programa qual arquivo ele irá abrir para comparar o hash. | O update faz a comparação do hash |
# Método "rb" é o método de leitura do modo binario
hash1.update(open(arquivo1, "rb").read())

hash2 = hashlib.new("ripemd160")
hash2.update(open(arquivo2, "rb").read())

#Comparação 
## Se um hash for diferente do outro:
### função digest(): 
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print("o hash do arquivo a.txt é: ", hash1.hexdigest())
    print("O hash do arquivo b.txt é: ", hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')    
    print("o hash do arquivo a.txt é: ", hash1.hexdigest())
    print("O hash do arquivo b.txt é: ", hash2.hexdigest())