# INTRODUÇAO AO GIT E GITHUB

    Curso oferecido pela DIO 
    Link do curso: https://web.dio.me/course/introducao-ao-git-e-ao-github/learning/75b9fe49-6ed4-4480-83a7-7e37fc356aa9?back=/track/geracao-tech-unimed-   bh-ciencia-de-dados&tab=undefined&moduleId=undefined
    Instrutor: Otavio Reis
    Site para instalar o git: https://git-scm.com/downloads

## Anotações sobre o que aprendi durante o curso.

    Linux: Abrir o terminal | Para liberar permissão: sudo su e digita a senha
    Windows: Abrir Git Bash

#### COMANDOS
    Listar os diretorios: ls 
    Pra navegar pra uma pasta especifica no sistema: cd /
    Para retroceder uma pasta: cd ..
    Para limpar o terminal: clear ou ctrl+L
    Criar pasta: mkdir <nome da pasta>
    Criar arquivos: echo conteudo > nome.txt   exemplo: echo hello > hello.txt
    Deletar um repositorio: rm -rf <nome_pasta>/
    Para saber qual a versao do git que esta se utilizando: git --version
    Para saber o status do arquivo: git status
    Para adicionar os arquivos em staged: git add *, git add <nome_arquivo>, git add .

#### SHA1
    A sigla SHA significa Secure Hash Algorithm (Algoritmo de Hash Seguro), é um conjunto 
    de funções hash criptográficas projetadas pela NSA (Agência de Segurança Nacional dos EUA). 
    Isso é relevante porque a saida dessa encriptação gera um conjunto de caracteres identificador 
    de 40 dígitos.  

#### OBJETOS FUNDAMENTAIS:
    - BLOBS
    - TREES
    - COMMITS


#### CONFIGURAÇÕES INICIAIS DO GIT 
    git config --global user.email "seuemail@gmail.com"
    git config --global user.name SeuUsuario 
    Para verificar as configurações: git config --list
    Para alterar as configurações: git config --global --unset user.email
                                   git config --global --unset user.name
                                   
#### CONFIGURANDO O GIT Á MAQUINA 
    Link da aula: https://web.dio.me/course/introducao-ao-git-e-ao-github/learning/7410b862-1989-421a-a48d-500db5857f53?back=/track/geracao-tech-unimed-bh-ciencia-de-dados&tab=undefined&moduleId=undefined
    
- Gerando a chave: 
    ssh-keygen -t ed25519 -C <seu_email> # Aqui ele ja vai mostrar onde sera gerada a chave
    
- Navegando até as chaves: 
    cd /home/xxxxxxx/.ssh
    ls
    cat id_ed25519.pub #PARA MOSTRAR O CONTEUDO DA CHAVE
        - Ir para o GitHub 
            Clica na foto de perfil 
                Settings
                    SSH and GPG keys
                        New SSH key : Coloca o nome da maquina e cola a CHAVE
        - Volta para o terminal 

- Inicializar o ssh-add (Entidade encarregada por pegar as chaves e lidar com elas):
            eval $(ssh-agent -s)
            ls
            ssh-add id_ed25519 #Aqui passamos a chave privada

#### CLONANDO UM REPOSITÓRIO 
    git clone passa_caminho 

#### PRIMEIROS COMANDOS COM GIT
    - INICIAR O GIT: 
        git init 
        ls
        ls -a #Mostra a pasta oculta
        cd ..

    


    
#### GERANDO ARQUIVO MARKDOWN
    # Editor de texto Typora: https://typora.io/#linux
    # Para deixar o texto grande (titulo)
    ### Para texto menores
    ** Negrito **
    _Italico_
    :nome_emoticon para emojis
     - (espeço - espaço para ficar com a bolinha na frente da frase)

    - CRIAR UM COMMIT 
        git add *
        git commit -m "commit inicial"

    
#### CONCEITOS
    GIT INIT: Inicializa / Cria o repositório dentro do diretório (pasta)
    UNTRACKED: São os arquivos que o Git ainda não tem ciencia deles
    TRACKED: São os arquivos que o Git ja tem ciencia deles. Dentro desse processo temos 3 etapas:
         - Unmodified: Arquivos que ainda não foram modificados
         - Modified: Arquivo que já sofreu alguma modificação 
         - Staged: Conceito chave, é onde ficam os arquivos que estão se preparando para fazer parte 
            de algum tipo de agrupamento (COMMIT)

    - Entendo o conceito na prática:
        cd workspace
        cd livro_receitas
        ls
        git status
        mkdir receitas
        ls
        mv strogonoff.md ./receitas/ #Movendo o arquivo strogonoff para a pasta receitas
        ls
        git status
        git add strogonoff.md receitas/  #Alterou o status dos arquivos para staged
        git status
        git commit -m "cria pasta receitas, move arquivo para receitas"  #Comitando os arquivos
        git status
        echo > README.md  #Criando o arquivo README.md
        git status

    
#### EMPURRAR O REPOSITÓRIO LOCAL PARA O REPOSITÓRIO REMOTO
    Primeiro criamos o diretório no GitHub. 
    No terminal: 
        git remote add origin git@github.com:SeuUsuario/Receitas.git
        git remote -v #Traz a lista de repositorios remotos
        git push origin master

    
#### RESOLVENDO CONFLITOS:
    Situação: Quando seu repositório ja esta no GitHub e você ou sua equipe efetua uma alteração. 
        git status 
        git add *
        ls
        git status
        git commit -m "Adiciona receita pavê"
        git push origin master # Deu erro de conflito, porque o repositório ja existe
        git pull origin master #Puxando o repositório para local, para o Git juntar os dois

    Para clonar o repositório remoto para o local:
        git clone https://github.com/python/cpython.git
        ls -a #Se tiver a pasta git. é porque é um repositório remoto 
        git remote -v #Para mostrar os repositórios
