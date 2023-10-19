import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/minha-foto.jpeg", width=250)

with col2:
    st.title("John Pereira")
    content = """
    Tenho me dedicado ao desenvolvimento web
    por mais de 4 anos, estão entre minhas
    competências personalização de temas
    WordPress, criação de templates a partir de
    wireframes e uma sólida competência em
    HTML, CSS, PHP e SQL.
    """
    st.info(content)

content2 = """
Abaixo voce pode ver alguns projetos feitos em Python. Fique a vontade para me contactar.
"""

st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
