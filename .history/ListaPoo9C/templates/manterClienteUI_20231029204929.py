import streamlit as st
import pandas as pd
from listaPoo9C.views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de clientes");
        tab1, tab2, tab3, tab4 = st.tabs["Listar", "Inserir", "Atualizar"]