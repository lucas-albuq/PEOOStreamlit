import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
  def main():
    st.header("Cadastro de Clientes")
    tab1 = st.tabs(["Inserir")
    with tab1: ManterClienteUI.inserir()

  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      if not View.cliente_inserir(nome, email, fone, senha):
        st.error("Já existe outro cliente com esse mesmo e-mail")
      else:
        st.success("Cliente inserido com sucesso")
        time.sleep(2)
        st.rerun()
