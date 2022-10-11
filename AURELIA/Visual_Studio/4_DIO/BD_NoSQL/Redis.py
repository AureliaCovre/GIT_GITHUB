
""" BANCOS CHAVE VALOR (KEY-VALUE)
Armazena um conjunto de dados, seja ele simples ou complexo, identificados por um identidicador exclusivo.
- Bom desempenho em aplicações em nuvem. 
- Menor capacidade de busca. 

USO: cache, sessão de usuário, carrinhos de compras
"""

""" Iremos utilizar o REDIS um banco de dados, cache, messageria e fila. 
- Alto desempenho;
- Estrutura de dados na memória.
- Versatilidade de uso.
- Replicação e persistência.

Quem usa: twitter, github, stackowerflow entre outros.
"""

# https://try.redis.io/

""" Criando users:
SET user1:nome "Bob Esponja"
SET user'{"name":"Patrick", "age":31}'
    
- Comando para inserir em uma lista:
LPUSH  user1:hobbies "Caçar agua viva"
LPUSH user1: hobbies "Comer hamburguer"  

- Busca pelo hobbies:
LINDEX user1:hobbies 0
LINDEX user1:hobbies 1

- Comando para listar todos os valores que temos dentro dessa lista ou para pegar o intervalo especifico 
que tem dentro dela:
LRANGE user1:hobbies 0 1

- Comando para descobrir o tipo de informação:
TYPE user1:name
TYPE user1:hobbies

- Comando para saber o tempo de expiração da chave que criamos:
TTL user1:name

- Comando para criar tempo de expiração:
SET user2:name "PATRICK" EX 30

- Comando para excluir o tempo de experiração:
PERSIST user2:name

- Consultas:
GET user2:name
EXISTS user2:name

- Comando de exclusão:
DEL user2:name

"""