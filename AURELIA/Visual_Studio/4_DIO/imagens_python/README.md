#Projeto: Pacote de Processamento de Imagens
##Autora do Projeto: Karina Kato
###Aula: Coding Lab PRO - Digital Innovation One
###Tecnologia: Python

Descrição
O pacote "image_processing-test" é usado para:

Módulo "Processamento":

Correspondência de histograma;
Similaridade estrutural;
Redimensionar imagem;
Módulo "Utils":

Ler imagem;
Salvar imagem;
Plotar imagem;
Resultado do gráfico;
Plotar histograma;
Passo a passo da configuração para hospedar um pacote em Python no Test Pypi
Instalação das últimas versões de "setuptools" e "wheel"
py -m pip install --user --upgrade setuptools wheel
Tenha certeza de que o arquivo no terminal seja o mesmo "setup.py"
C:\User\cafreitas\image-processing-package> py setup.py sdist bdist_wheel
Após a instalação, se as massas abaixo foram adicionadas ao projeto:

construir;
dist;
image_processing_test.egg-info.
Basta subir os arquivos, usando o Twine, para o Test Pypi:

py -m twine upload --repository testpypi dist/*
Após rodar o comando acima no terminal, será pedido para inserir o usuário e senha. Feito isso, o projeto ficará hospedado no Test Pypi.hospedá-lo no Pypi diretamente.
Aqui o objetivo não é usar o projeto da Karina para postar em meu perfil do Pypi pessoal, visto que o projeto é dela. Ainda não tenho nenhum projeto que possa ser utilizado como pacote.
No entanto, tenha em mente que o Test Pypi, como o próprio nome diz, é apenas um ambiente de testes. Para que o projeto está disponível publicamente como um pacote para ser usado, é necessário hospedar publicamente no site oficial do Pypi.
Instalação local, após hospedagem no Test Pypi
Instalação de dependências
pip install -r requirements.txt
Instalação do Pacote
Use o gerenciador de pip install -i https://test.pypi.org/simple/ image-processing-test pacotes para instalar image_processing-test

pip instalar teste de processamento de imagem
Como usar em qualquer projeto
do  teste de processamento de imagem . processamento combinação de combinação de importação . find_difference ( imagem1 , imagem2 )  


Autor (quem hospedou o projeto no Test Pypi)
Aurélia Covre

Licença
MIT