import streamlit as st
import pandas as pd
from listaPoo9C.views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de clientes");
        tab1, tab2, tab3, tab4 = st.tabs["Listar", "Inserir", "Atualizar", "Excluir"]
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            dic = []
            for obj in clientes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)