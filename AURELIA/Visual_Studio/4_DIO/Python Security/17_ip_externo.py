
"""  
- BIBLIOTECA RE: Permite Operações com expressões regulares.
- BIBLIOTECA JSON: Fornece operação de codificação e decodificação JSON
- URLLIB.REQUEST IMPORT URLOPEN: Funções e classes que ajudam a abrir URLs
http://ipinfo.io/json
"""

import json
from urllib.request import urlopen

url = "http://ipinfo.io/json"

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados["ip"]
org = dados["org"]
cid = dados["city"]
pais = dados["country"]
regiao = dados["region"]

print("Detalhes do IP externo: \n")
print("IP: {4}\nRegião: {1}\nPais: {2}\nCidade:{3}\nOrg.: {0}".format(org, regiao, pais, cid, ip) )