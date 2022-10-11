import os # Importa o módulo ou biblioteca os(Integra os programas e recursos do S.O)

print("#" * 60) # Imprimindo o # 60 vezes
ping_ip_ou_host = input("Digite o IP ou host a ser verificado: ") #Criamos uma variavel que vai receber do usuario um ip.
print("-" * 60) # Imprimindo o - 60 vezes

os.system("ping -n 6 {}".format(ping_ip_ou_host)) #Chamando system da biblioteca os - comando ping -n -num de pacotes que serão 6 {}
print("-" * 60) # Imprimindo o - 60 vezes
