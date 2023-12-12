# ACT Digital - Previsão do Tempo

Este projeto consiste em uma aplicação de backend desenvolvida em Python utilizando o mini-framework Flask para fornecer dados da previsão do tempo com base na API do OpenWeatherMap. Antes de executar a API, é necessário seguir alguns passos:

## Requisitos Iniciais

Antes de executar a aplicação, certifique-se de ter instalado o Python em sua máquina. Recomenda-se o uso de ambientes virtuais para isolar as dependências do projeto. Caso ainda não tenha instalado o `virtualenv`, pode instalá-lo usando o seguinte comando:

No Linux ou macOS:

    source venv/bin/activate

No Windows (PowerShell):

    .\venv\Scripts\Activate

## Instale as dependências:

    pip install -r requirements.txt

## Configuração da Chave da API do OpenWeatherMap
Antes de executar a aplicação, é necessário obter uma chave de API gratuita do OpenWeatherMap. Siga as instruções na página de inscrição para criar uma conta e obter sua chave.

Depois de obter a chave, defina-a como uma variável de ambiente. No Linux, você pode fazer isso usando o comando export no terminal:

    export OPENWEATHER_API_KEY=sua-chave-openweather

Execução da Aplicação
Agora que o ambiente está configurado e a chave da API do OpenWeatherMap está definida, você pode executar a aplicação Flask. Certifique-se de estar no ambiente virtual e execute:

## Utilizando a API

Após a execução bem-sucedida da aplicação, você pode acessar a API usando o endpoint /previsao para obter a previsão do tempo com base na cidade fornecida. Além disso, o histórico das consultas é acessível através do endpoint /historico.

## Observação:

_Lembre-se de que o histórico das consultas é armazenado em um banco de dados MongoDB. Certifique-se de ter um servidor MongoDB em execução para acessar o histórico_

