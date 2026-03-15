import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
import json 
from dotenv import load_dotenv
load_dotenv()

blobConnectionString = os.getenv("BLOB_CONNECTION_STRING")
blobContainerName = os.getenv("BLOB_CONTAINER_NAME")
blobAccountName = os.getenv("BLOB_ACCOUNT_NAME")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

st.title("Cadastro de Produtos")

product_name = st.text_input("Nome do Produto")
product_description = st.text_area("Descrição do Produto")
product_price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
product_image = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    container_client = blob_service_client.get_container_client(blobContainerName)
    blob_name = f"{uuid.uuid4()}_{file.name}"
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite=True)
    image_url = f"https://{blobAccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}"
    return image_url

def insert_product(name, description, price, image_url):
    try:
        conn = pymssql.connect(server=SQL_SERVER, database=SQL_DATABASE, user=SQL_USER, password=SQL_PASSWORD)
        cursor = conn.cursor()
        insert_query = "INSERT INTO Produtos (nome, descricao, preco, imagem_url) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (name, description, price, image_url))
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir produto: {e}")
        return False
    finally:
        if conn:
            conn.close()
        if cursor:
            cursor.close()    
    

if st.button("Cadastrar Produto"):
    if product_name and product_description and product_price and product_image:
        image_url = upload_blob(product_image)
        if insert_product(product_name, product_description, product_price, image_url):
            st.success("Produto cadastrado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")

def list_products():
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor(as_dict=True)
        query = "SELECT id, nome, descricao, preco, imagem_url FROM dbo.Produtos"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
        return []

def list_produtos_screen(): 
    products = list_products()
    if products:
            cards_por_linha = 3
            cols = st.columns(cards_por_linha)
            for i, product in enumerate(products):
                col = cols[i % cards_por_linha]
                with col:
                    st.markdown(f"### {product['nome']}")
                    st.write(f"**Descrição:** {product['descricao']}")
                    st.write(f"**Preço:** R$ {product['preco']:.2f}")
                    if product["imagem_url"]:
                        html_img = f'<img src="{product["imagem_url"]}" width="200" height="200" alt="Imagem do produto">'
                        st.markdown(html_img, unsafe_allow_html=True)
                    st.markdown("---")
                # A cada 'cards_por_linha' produtos, se ainda houver produtos, cria novas colunas
                if (i + 1) % cards_por_linha == 0 and (i + 1) < len(products):
                    cols = st.columns(cards_por_linha)
    else:
            st.info("Nenhum produto encontrado.")

st.header("Listagem dos Produtos")


if st.button("Listar Produtos"):
    list_produtos_screen()

def clear_products():
    conn = None
    cursor = None
    try:
        conn = pymssql.connect(server=SQL_SERVER, database=SQL_DATABASE, user=SQL_USER, password=SQL_PASSWORD)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Products")  # Padronize para "Products"
        conn.commit()
        return True
    except Exception as e:
        st.error(f"Erro ao limpar produtos: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if st.button("Limpar Produtos"):
    if clear_products():
        st.success("Todos os produtos foram removidos.")
   

