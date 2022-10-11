import random 
import string

# Aqui estamos definindo o tamanho da senha 
tamanho = 16

# Estrutura da senha que será gerada | método ascii.letters: gera letras maiuscula e miniscula
chars = string.ascii_letters + string.digits + "!@#$%&*()_-+,.;:"

#
rnd = random.SystemRandom()

#Gerando a senha
print("".join(rnd.choice(chars) for i in range(tamanho)))

