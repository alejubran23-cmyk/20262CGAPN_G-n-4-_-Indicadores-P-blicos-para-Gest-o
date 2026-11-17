import pandas as pd
import streamlit as st

def classifica_porte(total):
    if total <= 200:
        return "Pequena"
    elif total <= 400:
        return "Média"
    else:
        return "Grande"

censo = pd.read_csv("escolas_sp_regioes_2024_geo.csv")
censo["porte"] = censo["matriculas"].apply(classifica_porte)


st.title("Painel de Escolas de Regiões de SP")
st.caption("Adaptado do Censo Escolar 2024 (INEP)")

regiao = st.selectbox(
    "Escolha a Região",
    ["Todas", "Região Metropolitana de SP",
     "Baixada Santista", "Litoral Norte", "Vale do Ribeira"]
)

if regiao != "Todas":
    censo = censo[censo["regiao"] == regiao]

porte_escolhido = st.selectbox(
    "Escolha o porte",
    ["Todos", "Pequena", "Média", "Grande"]
)

if porte_escolhido != "Todos":
    censo = censo[censo["porte"] == porte_escolhido]

municipio_escolhido = st.selectbox(
    "Escolha o município",
    ["Todos"] + sorted(censo["municipio"].unique())
)

if municipio_escolhido != "Todos":
    censo = censo[censo["municipio"] == municipio_escolhido]

localizacao_escolhida = st.selectbox(
    "Escolha a localização",
    ["Todas"] + sorted(censo["localizacao"].unique())
)

if localizacao_escolhida != "Todas":
    censo = censo[censo["localizacao"] == localizacao_escolhida]

dependencia_escolhida = st.selectbox(
    "Escolha a dependência administrativa",
    ["Todas"] + sorted(censo["dependencia"].unique())
)

if dependencia_escolhida != "Todas":
    censo = censo[censo["dependencia"] == dependencia_escolhida]

agua_potavel_escolhida = st.selectbox(
    "A escola fornece água potável?",
    ["Todas"] + sorted(censo["agua_potavel"].unique())
)

if agua_potavel_escolhida != "Todas":
    censo = censo[censo["agua_potavel"] == agua_potavel_escolhida]

etapas_ensino = {
    "Educação Infantil": "mat_infantil",
    "Ensino Fundamental": "mat_fundamental",
    "Ensino Médio": "mat_medio"
}

etapas_disponiveis = [
    etapa for etapa, coluna in etapas_ensino.items()
    if (censo[coluna] > 0).any()
]

etapa_escolhida = st.selectbox(
    "Escolha a etapa de ensino",
    ["Todas"] + etapas_disponiveis
)

if etapa_escolhida != "Todas":
    coluna_etapa = etapas_ensino[etapa_escolhida]
    censo = censo[censo[coluna_etapa] > 0]

col1, col2 = st.columns(2)
col1.metric("Qtde de Escolas", len(censo))
col2.metric("Total de Matrículas", censo["matriculas"].sum())


st.subheader("Escolas por Porte")
st.bar_chart(censo["porte"].value_counts())

st.subheader("Escolas por Abastecimento de Agua")
st.bar_chart(censo["agua"].value_counts())

st.subheader("Escolas por dependência administrativa")
st.bar_chart(censo["dependencia"].value_counts())

st.subheader("Escolas por fonte de energia")
st.bar_chart(censo["energia"].value_counts())

st.subheader("Escolas por localização diferenciada")
st.bar_chart(censo["loc_diferenciada"].value_counts())

st.subheader("Escolas por esgotamento sanitário")
st.bar_chart(censo["esgoto"].value_counts())

st.subheader("Escolas por destinação do lixo")
st.bar_chart(censo["lixo"].value_counts())

st.subheader("Escolas por localização urbana ou rural")
st.bar_chart(censo["localizacao"].value_counts())

st.subheader("Matrículas por etapa de ensino")

matriculas_por_etapa = censo[
    ["mat_infantil", "mat_fundamental", "mat_medio"]
].sum().rename(index={
    "mat_infantil": "Educação Infantil",
    "mat_fundamental": "Ensino Fundamental",
    "mat_medio": "Ensino Médio"
})

st.bar_chart(matriculas_por_etapa)
st.caption("O gráfico mostra as três etapas detalhadas na base. O indicador Total de Matrículas usa o total registrado por escola.")

st.subheader("Mapa das escolas")
st.map(censo[["latitude", "longitude"]])

st.subheader("Lista das escolas")
st.dataframe(censo[["municipio", "escola", "matriculas", "porte"]])