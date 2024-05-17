# Turtlebot controlado por CLI

Este repositório contém pacotes ROS que permitem controlar um turtlebot através de uma CLI.

## Pré-requisitos

Para rodar este projeto, você precisará ter o ROS 2, o `turtlesim` e o Python 3.8 ou superior instalados no seu sistema.

## Instruções de execução

Primeiramente rode no seu terminal o seguinte comando para clonar o repositório:

`git clone https://github.com/olin-med/entrega_prova.git`

Entre no diretório do projeto:

`cd workspace_prova`

Em seguida, rode os dois comandos abaixo para buildar os pacotes e dar source no script de configuração do workspace:

`colcon buld`

`source install/local_setup.bash`

Agora abra uma nova janela no seu terminal.

Na primeira janela rode o seguinte comando:

`ros2 run movie-publish publisher`

E, por fim, basta rodar na segunda janela:

`ros2 run cli cli`

Pronto! Uma janela deve abrir na qual a tartaruga spawnará e você conseguirá controlá-la enviando comandos pela CLI.

## Vídeo do projeto em execução:


Este código foi desenvolvido por Ólin Medeiros Costa.
