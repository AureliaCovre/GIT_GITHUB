""" --- BANCOS DE DADOS BASEADOS EM DOCUMENTO ---

    Dados e documentos auto contidos e auto descritivos.
    Permite redundância e inconsistência. 
    Livre de esquemas podendo utilizar JSON, XML entre outros.
    
Exemplos: MongoDB, Couchbase, Firebase Realtime Database, CouchDB, Realm, Google cloud Firestore.    


    --- INTRODUÇÃO AO MONGODB ---
    
- Código aberto
- Alta performance
- Schema-free
- Utiliza json para armazenamento dos dados
- Suporte a indices
- Auto-Sharding
- Map-Reduce (Ferramenta de consulta e agregação, um diferencial qdo é necessario processar qde volume de dados)
- GridFS (armazenamento de arquivos)

* FERRAMENTAS:
Document ==> Tupla/Registro
Collection == Tabela
Embedding/linking ==> Join 

* QUANDO USAR O MONGODB:
- Grande volumes de dados
- Dados não necessariamente estruturados

* QUANDO NÃO UTILIZAR:
- Necessidade de relacionamentos / joins
- Propriedades ACID e transações são importantes
- Curiosidade: Diversas entidades de pagamento não homologam sistemas cujo dados financeiros dos clientes não 
estejam em bancos de dados relacionais tradicionais. 
"""

# https://hub.docker.com/
# https://robomongo.org/

""" --- INTRODUÇÃO AO MONGODB CLOUD ----

https://www.mongodb.com/try
usuario dio / senha dio




"""



