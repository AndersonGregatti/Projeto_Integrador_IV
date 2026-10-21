"""
Registro de Frequência — Rede Municipal de Cubatão
App Streamlit que embute a página HTML `registro_frequencia_cubatao.html`.

Como rodar localmente:
    pip install -r requirements.txt
    streamlit run registro_app.py

Para alterar o visual ou o comportamento (anos, meses, turnos, nomes dos alunos),
edite o arquivo `registro_frequencia_cubatao.html`. Este arquivo .py só carrega a página.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Registro de Frequência — Rede Municipal de Cubatão",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .block-container {padding-top: 1rem; padding-bottom: 0; padding-left: 1rem; padding-right: 1rem;}
    header[data-testid="stHeader"] {display: none;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# O HTML deve ficar na mesma pasta deste arquivo (e no mesmo nível no GitHub)
ARQUIVO = Path(__file__).parent / "registro_frequencia_cubatao.html"

# Altura do quadro onde a página é exibida (aumente se aparecer rolagem dupla)
ALTURA_PX = 1400

if not ARQUIVO.exists():
    st.error(f"Arquivo não encontrado: {ARQUIVO.name}. Coloque-o na mesma pasta de registro_app.py.")
    st.stop()

components.html(ARQUIVO.read_text(encoding="utf-8"), height=ALTURA_PX, scrolling=True)
