📦 Desafio DIO – E-Commerce na Azure Cloud

📌 Descrição do Projeto

Este projeto foi desenvolvido como parte do Bootcamp Microsoft Azure Cloud Native 2026 da DIO, com o objetivo de criar uma aplicação de cadastro e gerenciamento de produtos de e-commerce na nuvem.

A solução utiliza serviços da Microsoft Azure para garantir escalabilidade, disponibilidade e segurança, integrando armazenamento de imagens e banco de dados em nuvem com uma interface web simples construída em Python.

🎯 Objetivos de Aprendizado

Aplicar conceitos de Cloud Computing

Utilizar serviços reais da Microsoft Azure

Integrar backend + banco + storage

Criar aplicações web simples com Streamlit

Trabalhar com segurança usando variáveis de ambiente

🧱 Arquitetura do Projeto

O sistema segue uma arquitetura simples baseada em três camadas principais:

🔹 1. Interface (Frontend)

Desenvolvida com Streamlit

Permite:

  Cadastro de produtos
  
  Upload de imagens
  
  Listagem de produtos

🔹 2. Backend (Lógica da Aplicação)

Responsável por:

  Processar os dados do formulário
  
  Fazer upload das imagens
  
  Inserir e consultar dados no banco

Principais funções:

upload_blob()

→ Envia imagens para o Azure Blob Storage
insert_product()

→ Insere produtos no Azure SQL Database
list_products()

→ Consulta produtos no banco
list_produtos_screen()

→ Exibe produtos em formato visual (cards)

🔹 3. Persistência de Dados

🗄️ Banco de Dados (Azure SQL)

CREATE TABLE Produtos(
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255),
    descricao NVARCHAR(MAX),
    preco DECIMAL(18,2),
    imagem_url NVARCHAR(2083)
)

🖼️ Armazenamento de Imagens

Utiliza Azure Blob Storage

Cada imagem recebe um nome único com UUID

A URL da imagem é armazenada no banco

☁️ Tecnologias e Serviços Utilizados

Microsoft Azure: 

  Azure SQL Database
  
  Azure Blob Storage

Python: 

  Streamlit (interface web)
  
  pymssql (conexão com banco SQL)
  
  azure-storage-blob (upload de imagens)
  
  dotenv (variáveis de ambiente)

VS Code

🚀 Funcionalidades

Cadastro de produtos

Upload de imagens para a nuvem

Armazenamento de dados no Azure SQL

Listagem de produtos em formato visual

Integração completa com serviços cloud

Remoção de produtos (limpeza do banco)

▶️ Como Executar o Projeto

1. Clone o repositório: git clone https://github.com/seu-usuario/seu-repositorio.git

2. Instale as dependências: pip install streamlit azure-storage-blob pymssql python-dotenv

3. Configure o arquivo .env

BLOB_CONNECTION_STRING=...

BLOB_CONTAINER_NAME=...

BLOB_ACCOUNT_NAME=...

SQL_SERVER=...

SQL_DATABASE=...

SQL_USER=...

SQL_PASSWORD=...

4. Execute a aplicação

streamlit run app.py

🚀 Resultados

Ao final do desafio, foi possível compreender como a nuvem pode ser utilizada para hospedar aplicações de e-commerce, permitindo escalabilidade, segurança e gerenciamento simplificado da infraestrutura.
