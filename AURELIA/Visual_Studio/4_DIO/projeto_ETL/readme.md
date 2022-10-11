## PROJETO TRATAMENTO ETL COM PYTHON 

O objetivo principal desse projeto é o aperfeiçoamento no conhecimento do processo de ETL do início até o fim, passando por todas as etapas. Assim como o conhecimento de novas ferramentas e bibliotecas que são utilizadas para desenvolver e facilitar o processo de desenvolvimento do processo de ETL. Extraímos os dados, transformá-los para gerar novos dados e resultados e carregar em novos repositórios de dados para que sejam utilizados por ferramentas, pessoas e algoritmos. Criamos novos modelos de dados para futuras representação e facilitação do entendimento dessas informações.

Liguagem: Python / 
Bibliotecas: Pandas e Pandera / 
Ferramenta: Jupyter


O QUE É O ETL:

**ETL –  Extract, Transform e Load** (Extração, Transformação e Carregamento de dados).
Extract: Os dados podem ser extraídos de diferentes fontes de dados, podendo ser base de dados (internas e externas), arquivos (csv, Jason), Excel, Texto, PDF, API (facebook, twitter), BI e etc. E podem ser processadas em lotes (através do processo Batch) ou Real Time (tempo real).
Transform:  Os dados são propagados para a área de preparação, onde são transformados e limpos.
Load: Carregados no data warehouse.

POR QUE UTILIZAR PROCESSO ETL?

Quando a empresa precisa tomar uma decisão ela analisa os dados, mas por vezes esses dados estão disponíveis em diferentes fontes, podendo ser até mesmo em fontes externas. O processo ETL faz a junção, organização e limpeza de forma consistente, confiável e íntegra.

TERMOS TÉCNICOS:
- _DATA SOURCES:_ As diferentes fontes de dados que armazenam os dados que serão extraídos e carregados para data warehouse.
- _PIPELINE_ (Segmentação dos processos):  Dentro desse contexto acontece:  Validação, Limpeza, Transformação, Agregação, Normalização e Carregamento.
- _DATA FLOW_: caminho dos dados, até serem carregados e disponibilizados para ferramentas de análises de dados.
- _BI RESULTS_: Ferramentas de análise: OLAP Analysis, Data Mining, Data Visualization, Reports, Dashboards e Alerts

FERRAMENTAS / PACOTES PARA PYTHON: 
- _Apache Airflow_: Concebido pelos Engenheiros do Airbnb. Utilizada também pela Tesla e Spotify
- _Luigi_: Construido pela Spotify. Ele permite a construção de ferramentas de visualização, recuperação de falhas de forma mais fácil e tranquila, ele também tem uma interface por linha de comando. 
- _Bonobo_: Kit de ferramentas de processamento para se trabalhar com etl em python de forma rápida e sua principal característica é ele permite executar processos em paralelo. 
- _Bubbles_: Conjunto de ferramentas para processar, auditar e excepcionar dados. O seu foco esta na compreensão e na transparência do processo de ETL.
- _Petl_: Pacote ETL de uso geral, projetado para facilidade do uso e construção do processo ETL. Ele é fácil para se trabalhar, mas ele não consegue trabalhar com dados muito grandes. 
- _Pandas_:  Muito parecido com o Petl , mas o Pandas tem um conjunto de dataframes e ele pode ser utilizado com uma quantidade maior de dados que o Petl.

FONTE DOS DADOS:
- **CENIPA** - Centro de Investigação e Prevenção de Acidentes Aeronáuticos
- https://www2.fab.mil.br/cenipa/
-	Clique em: Acesso a informação /                 Dados abertos / Base de dados de ocorrências aeronáuticas.

Nessa base de dados poderemos encontrar informações sobre as aeronaves envolvidas nessas ocorrências, as fatalidades, local, data, horário dos eventos e informações típicas de investigações de acidentes. Todas essas informações estão disponíveis em arquivos CSV e para entender como esses dados estão relacionados é importante conhecer o modelo de dados fornecido pelo próprio CENIPA, essa etapa também pode ser chamada de análise exploratória. 

No nosso projeto trabalhamos com as ocorrências.
- _codigo_ocorrencia1 = ocorrência_tipo_
- _codigo_ocorrencia2 = aeronave_
- _codigo_ocorrencia3 = fator_contribuinte_
- _codigo_ocorrencia4 = recomendação_
