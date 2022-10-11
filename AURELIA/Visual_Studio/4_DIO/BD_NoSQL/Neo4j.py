""" ----- OBJETIVO DO CURSO ----
    Introdução ao mundo NoSQL, apresentar os tipos de bancos NoSQL assim como realizar pequenas 
operações em alguns deles com enfâse no MongoDB no qual iremos desde sua instalação, opções de uso 
na nuvem e operações de manipulação de dados.
"""

""" GRAFOS 
Grafos: são estruturas matematicas composta por nós e vertices. Quando trazemos essa estrutura para dentro do
nosso bando de dados, temos basicamente: Nós compondo nossos dados e Vertices compondo nossos relacionamentos.
São muito comuns em detecção de fraudes, mecanismos de recomendação, redes sociais, sistemas de arquivo, games...

Bancos orientados a grafos mais utilizados: Neo4j, JanusGraph e TigerGraph
"""

""" Vamos criar uma estrutura de registros que compõem os dados de uma rede social utilizando um sandbox do Neo4j
Ele utiliza a linguagem Cypher como linguagem de estruturação de seus dados"""

""" Para criar um cliente (banco Neo4j):
CREATE(:Client {name : "Bob Esponja", age: 28, hobbies: ["Caça agua=viva, Comer hamburguers"]})

    Selecionar o cliente:
MATCH (bob_esponja) RETURN bob_esponja;
MATCH (todos) RETURN todos;

    Criando um objeto:
CREATE(:Object)
    
    Criando um novo cliente com relacionamento. na primeira linha entre () estamos criando o nó. A partir do hífen
estamos definindo o relacionamento. 
CREATE(:Client{name: "Lula Molusco", age: 30, hobbies: ["Tocar clarinete"]}) 
-[:Bloqueado]->(:Client {name: "Patrick", hobbies: ["Caçar agua viva"]})

    Excluindo um relacionamento:
MATCH (lula:Client {name: "Lula Molusco"})-[relaciona:Bloqueado]-() DELETE relaciona
    
    
    Excluindo um nó:
MATCH (lula:Client {name: "Lula Molusco"}) DELETE lula;

    Atualizando um nó:
MATCH(patrick:Client {name:"Patrick"}) SET patrick.hobbies = ["Caçar agua viva"];
"""


