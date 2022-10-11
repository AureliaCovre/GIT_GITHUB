import ipaddress

ip = "192.168.0.1"
ip_rede = "192.168.0.0/24"

endereco = ipaddress.ip_address(ip)
end_rede = ipaddress.ip_network(ip_rede)

print("IP: ", endereco + 256)
print("Rede: ", end_rede)

#Para imprimir todos os ips da rede 24
for ip_rede in end_rede:
    print(end_rede)