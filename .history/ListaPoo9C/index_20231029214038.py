from ListaPoo9C.templates.manterclienteUI import ManterClienteUI
from ListaPoo9C.templates.manterservicoUI import ManterServicoUI
from ListaPoo9C.templates.manteragendaUI import ManterAgendaUI
from ListaPoo9C.templates.abriragendaUI import AbrirAgendaUI

import streamlit as st

class IndexUI:
      
    def sidebar():
      op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda", "Abrir Agenda do Dia"])
      if op == "Manter Clientes": ManterClienteUI.main()
      if op == "Manter Serviços": ManterServicoUI.main()
      if op == "Manter Agenda": ManterAgendaUI.main()
      if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()

      #if op == "Manter Clientes": st.session_state["page"] = "manter_clienteUI"

    def main():
      IndexUI.sidebar()

      #if "page" not in st.session_state: st.session_state["page"] = "equacaoUI"
      #if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()

IndexUI.main()