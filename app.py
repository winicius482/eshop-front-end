import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Conectar ao MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["crud_db"]
collection = db["clientes"]

# Sidebar com opções
menu = ["Criar", "Listar", "Atualizar", "Deletar"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Criar":
    st.subheader("Adicionar Cliente")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    if st.button("Salvar"):
        if nome and email:
            collection.insert_one({"nome": nome, "email": email})
            st.success("Cliente criado com sucesso!")
        else:
            st.error("Preencha todos os campos.")

elif choice == "Listar":
    st.subheader("Lista de Clientes")
    data = list(collection.find({}, {"_id": 0}))
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.info("Nenhum cliente cadastrado.")

elif choice == "Atualizar":
    st.subheader("Atualizar Cliente")
    clientes = list(collection.find())
    cliente_map = {f"{c['_id']} - {c['nome']}": c for c in clientes}
    if clientes:
        sel = st.selectbox("Selecione o cliente", list(cliente_map.keys()))
        novo_nome = st.text_input("Novo Nome", cliente_map[sel]["nome"])
        novo_email = st.text_input("Novo Email", cliente_map[sel]["email"])
        if st.button("Atualizar"):
            collection.update_one(
                {"_id": cliente_map[sel]["_id"]},
                {"$set": {"nome": novo_nome, "email": novo_email}}
            )
            st.success("Cliente atualizado com sucesso!")
    else:
        st.info("Nenhum cliente para atualizar.")

elif choice == "Deletar":
    st.subheader("Deletar Cliente")
    clientes = list(collection.find())
    cliente_map = {f"{c['_id']} - {c['nome']}": c for c in clientes}
    if clientes:
        sel = st.selectbox("Selecione o cliente", list(cliente_map.keys()))
        if st.button("Deletar"):
            collection.delete_one({"_id": cliente_map[sel]["_id"]})
            st.success("Cliente deletado com sucesso!")
    else:
        st.info("Nenhum cliente para deletar.")
