# 📱 WhatsApp Bot

Este é um projeto de um bot de WhatsApp desenvolvido em Python que utiliza a biblioteca Selenium para automatizar o envio de mensagens pelo WhatsApp Web.

## 🚀 Instalação

1. Faça o download do repositório:
```
git clone https://github.com/seu-usuario/whatsapp-bot.git
```

2. Instale as dependências:
```
pip install -r requirements.txt
```

3. Crie um arquivo `config.ini` na raiz do projeto e preencha com as informações necessárias (veja o exemplo abaixo):
```ini
[CHROME]
profile_path = /home/user/.config/google-chrome/Profile 1/
```

4. Inicie o bot:
```
python whatsapp_bot.py arquivo_de_entrada.txt
```

## 🤖 Funcionalidades

O bot lê um arquivo de entrada com uma mensagem e um destinatário e envia a mensagem para o destinatário através do WhatsApp Web.

## 📝 Arquivo de entrada

O arquivo de entrada deve ter o seguinte formato:
```
#para: <nome ou número do destinatário>
#mensagem: <mensagem a ser enviada>
***
```

## 📝 Arquivo de saída

O bot salva um arquivo de saída com o registro de todas as mensagens enviadas. O arquivo tem o seguinte formato:
```
<destinatário>, <mensagem>, <data e hora do envio>
```

## 📝 Exemplo de uso

Suponha que você queira enviar uma mensagem para o número de telefone +55 11 1234-5678 com a mensagem "Olá, mundo!". Você deve criar um arquivo de entrada com o seguinte conteúdo:
```
#para: +55 11 1234-5678
#mensagem: Olá, mundo!
***
```

E então executar o bot com o comando:
```
python whatsapp_bot.py arquivo_de_entrada.txt
```

# 🚀 Desenvolvimento de Novas Funcionalidades

👨‍💻 Com o objetivo de tornar o whatsapp_bot ainda mais útil e eficiente, estamos trabalhando no desenvolvimento de algumas novas funcionalidades. Abaixo, apresentamos um resumo de cada uma dessas funcionalidades, bem como do processo de criação de cada uma delas:

## 📝 Futuras funcionalidades

- Implementação de um comando para enviar imagens e arquivos
- Integração com APIs de inteligência artificial para respostas automáticas

## 1. Integração com API externa

🔗 A primeira funcionalidade que estamos trabalhando é a integração do whatsapp_bot com uma API externa, que permitirá buscar informações adicionais a serem incluídas nas mensagens. Para isso, o processo de criação da funcionalidade incluirá os seguintes passos:

- Definição dos endpoints da API e dos dados a serem buscados;
- Criação de uma função para fazer a chamada à API e obter as informações necessárias;
- Integração da função criada com as funcionalidades de envio de mensagens do whatsapp_bot.

## 2. Busca em banco de dados

🔍 Além da busca em API externa, estamos trabalhando também na possibilidade de buscar informações em um banco de dados. Para isso, o processo de criação da funcionalidade incluirá os seguintes passos:

- Definição da estrutura do banco de dados e das tabelas a serem utilizadas;
- Criação de uma função para buscar as informações necessárias no banco de dados;
- Integração da função criada com as funcionalidades de envio de mensagens do whatsapp_bot.

## 3. Identificação de imagens

📷 Outra funcionalidade que estamos trabalhando é a identificação de imagens enviadas para o whatsapp_bot. Com isso, será possível buscar informações adicionais sobre as imagens e incluí-las nas respostas do bot. Para isso, o processo de criação da funcionalidade incluirá os seguintes passos:

- Definição dos serviços de reconhecimento de imagem a serem utilizados;
- Criação de uma função para fazer a busca das informações necessárias com base na imagem recebida;
- Integração da função criada com as funcionalidades de envio de mensagens do whatsapp_bot.

## 4. Envio de arquivos

📁 Por fim, estamos trabalhando na possibilidade de envio de arquivos pelo whatsapp_bot. Com isso, os usuários poderão enviar arquivos para o bot e receber arquivos em resposta. Para isso, o processo de criação da funcionalidade incluirá os seguintes passos:

- Definição dos tipos de arquivo que poderão ser enviados e recebidos;
- Criação de uma função para lidar com o envio e recebimento de arquivos;
- Integração da função criada com as funcionalidades de envio de mensagens do whatsapp_bot.

🔜 Em breve, esperamos ter todas essas funcionalidades implementadas e funcionando corretamente no whatsapp_bot, para torná-lo ainda mais completo e útil para nossos usuários!

