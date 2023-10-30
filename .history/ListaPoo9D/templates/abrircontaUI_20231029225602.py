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

  def atualizar():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Atualização de Clientes", clientes)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      email = st.text_input("Informe o novo e-mail", op.get_email())
      fone = st.text_input("Informe o novo fone", op.get_fone())
      senha = st.text_input("Informe a nova senha", op.get_senha())
      if st.button("Atualizar"):
        id = op.get_id()
        if not View.cliente_atualizar(id, nome, email, fone):
          st.error("Já existe outro cliente com esse mesmo e-mail")
        else:
          st.success("Cliente atualizado com sucesso")
          time.sleep(2)
          st.rerun()

  def excluir():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Exclusão de Clientes", clientes)
      if st.button("Excluir"):
        id = op.get_id()
        View.cliente_excluir(id)
        st.success("Cliente excluído com sucesso")
        time.sleep(2)
        st.rerun()