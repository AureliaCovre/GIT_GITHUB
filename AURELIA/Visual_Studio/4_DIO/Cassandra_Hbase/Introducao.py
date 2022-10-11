""" EXPLORANDO O PODER DO NOSQL COM APACHE CASSANDRA E APACHE HBASE - Valdir Sevaios"""

""" INTRODUÇÃO NoSQL

* SIGNIFICADOS:
- NoSQL = "No SQl" , "Não SQL" ou "Não relacional"
- NoSQL = "Not Only SQL"

Termo genérico para representar os bancos de dados não relacionais. 

O NoSQL emergiu como uma alternatica de banco de dados não relacionado, normalmente evitando operações de "join",
é distribuido, open-source, escalável na horizontal, livre de modelagens ou schema (não é necessario fixar modelos
para as tabelas), suporta replicação, acesso via API de operações e eventualmente consistente.
"""

"""    Relacional x NoSQL   

Quando considerar NoSQL:
- Carga de trabalho de alto volume que exigem grande escala
- Carga de trabalho não exigem garantias do ACID
- Os dados não dinâmicos e frequentemente alterados
- Os dados podem ser expressos sem relações (joins)
- Alta velocidade de gravação e a segurança de gravação não é critica
- Consulta de dados é simples e tende a ser simples
- dados exigemuma ampla distribuição geografica

Quando considerar Relacional:
- Carga de trabalho é consistente e requer escaa média para grande 
- Garantias de ACID são necessárias
- Dados são previsiveis e altamente estriturados
- Os dados são expressos de maneira relacional
- A garantia de gravação é um requisito
- Consultas e relatórios complexos
- Usuarios são mais centralizados
"""

""" TEOREMA DE CAP

    O teorema CAP ou teorema de Brewer indica que o armazenamento de dados distribuídos só podem atender dois 
dos três atributos: CONSISTENCIA, DISPONIBILIDADE, PARTIÇÃO TOLERANTE A FALHAS.

    Tanto Haddop e HBase atendem CP, porque possuem um ponto de falha que é respectivamente o NomedNOde e Hmaster
que não possuem redundancia dos dados dos proprios serviços para todos os nós do cluter.
    
CA = Consistency & Availability
- MySQL 
- PostgreSQL

AP = Availability & Partion tolerance
- Riak
- Cassandra
- CouchDb
- DynamoDB

CP = Consistency & Partion tolerance
- Hbase
- MongoDB
- Regis
- Mencache    
"""

""" POR QUÊ NOSQL NO BIG DATA

Limitações do Haddop:
    - Haddop (MapReduce) pode executar apenas processamento batch e os dados são acessados de forma sequencial, 
    isso significa que é necessario percorrer todo o conjunto de arquivos (scan search) mesmo para os jobs mais 
    simples. 
    
Cenário:
    - Um grande conjunto de dados (dataset) quando processado com um outro conjunto de dados, ambos serão 
    processados de maneira sequencial, nsse momento uma nova solução é necessaria para acessar qualquer
    ponto do dataser (linhas) e que leve um tempo menor para retornar. 
    - Aplicações como Hbase, Cassandra, Dynamo e MongoDB, etc, são bancos de dados que armazenam grandes
    quantidade de dados e os acessos á esses dados são realizados de forma aleatória em termos de posição
    do registro e do tempo.   
"""

""" O QUE É O APACHE HBASE
Hbase é um banco de dados distribuido e orientado a colunas (Column Family ou Wide Column)

Uma definição mais tecnica:
    O armazenamento do Hbase é um esparso, distribuido, persistente, multidemensional e ordenado MAP. 
    
    As maiores descantadens do Hbase é não ter uma limguagem própria de SQl, não suportar índices em colunas
    fora do rowkey e não suportar tabelas secundarias de  indices.
    A maior vantagem é a facilidade e integração com o ecossistemas Hadoop.
    
Conceitos:
    Map é indexado por uma linha chave (row Key), coluna chave (column key), e uma coluna timestamp.
    
    Cada valor no Map é interpretado como um vetor de bytes (array of bytes)
    
    O array of bytes ns permite gravar portanto qualquer informçõa se for necessario, inclusive documentos, 
    arquivos JSON, CSV, etc.
    
    Portanto podemos entender uqe o núcleo de dados do Habse é um MAP.
    
    Na maioria das linguagens de programação essas abstração de estrutura de dados existe e pode ser representada
    como um conjunto de chaves e conjunto de valores. Cada chave é associada à um valor.
"""

