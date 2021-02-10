# Desafio Cesar

## Como rodar o projeto

#### 1. Clone este repositório no terminal

  git clone https://github.com/mailtonfcarvalho/desafio_cesar.git

#### 2. Crie um ambiente virtual usando o pipenv

  Caso não possua o "pipenv" em sua maquina execute o seguinte comando para garantir que o pip esteja instalado em seu sistema:

$ pip --version

Instale o pipenv executando o seguinte comando:

$ pip install --user pipenv

No terminal, com o "pipenv" instalado execulte o comando abaixo para ativar o ambiente virtual

$ pipenv install requests

$ pipenv shell

#### 3. Instale as dependêcias do projeto

$ pipenv install selenium==3.14.1
$ pipenv install webdriver-manager
$ pipenv install numpy==1.19.5

#### 4. Ainda no terminal, execute o seguinte comando:

Execute o comando abaixo para Atividade de automação 1

$ python automation1.py

Execute o comando abaixo para Atividade de automação 2

$ python automation2.py
