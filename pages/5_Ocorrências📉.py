import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Carregar o arquivo CSV,,,,,,,,,,,,,,,,,,,,,,,,,,,,\
@st.cache_data
def load_data():
    df = pd.read_csv("Brazil Total Aeronautical Occurrences 2010 - 2021.csv")
    return df


# Função para análise exploratória
def exploratory_data_analysis(df):
    # Visualizar as primeiras linhas do DataFrame
    st.write("Análise Geral de Ocorrências:")
    st.dataframe(df.head())

    # Estatísticas descritivas do DataFrame
    st.write("Estatísticas descritivas do DataFrame:")
    st.write(df.describe())

    # Contagem de ocorrências por classificação
    st.write("Contagem de ocorrências por classificação:")
    st.write(df['ocorrencia_classificacao'].value_counts())

    # Gráfico de barras da contagem de ocorrências por classificação
    st.write("Gráfico de barras da contagem de ocorrências por classificação:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df, x='ocorrencia_classificacao', ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    # Mostrando outras questões
    st.write("Outras questões:")
    st.write("Latitude das ocorrências:")
    st.write(df['ocorrencia_latitude'])
    st.write("Longitude das ocorrências:")
    st.write(df['ocorrencia_longitude'])
    st.write("Cidade das ocorrências:")
    st.write(df['ocorrencia_cidade'])
    st.write("UF das ocorrências:")
    st.write(df['ocorrencia_uf'])
    st.write("País das ocorrências:")
    st.write(df['ocorrencia_pais'])
    st.write("Aeródromo das ocorrências:")
    st.write(df['ocorrencia_aerodromo'])
    st.write("Dia das ocorrências:")
    st.write(df['ocorrencia_dia'])
    st.write("Hora das ocorrências:")
    st.write(df['ocorrencia_hora'])
    st.write("Investigação de aeronave liberada:")
    st.write(df['investigacao_aeronave_liberada'])


# Configurações gerais do app
st.set_page_config(page_title="Análise de Ocorrências Aeronáuticas",
                   layout='wide')

#Seção para falar Sobre SIPAE
st.title(
    "Filosofia da SIPAE (Sistema de Investigação e prevenção de Acidentes Aeronáuticos"
)
st.write(
    "Todo acidente pode (e deve) ser evitado. Todo acidente resulta de uma seqüência de eventos e nunca de uma “causa” isolada. Todo acidente tem um precedente. Prevenção de acidente é uma tarefa que requer mobilização geral."
)
st.image(
    'https://s2-g1.glbimg.com/UzCqkeNL27d252n-2mrqELTgnIU=/0x0:1600x1200/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/u/W/RzQvBlQ1elqlaHTlzEQA/queda-aviao.jpeg'
)

# Título da página
st.title("Análise de Ocorrências Aeronáuticas")
st.subheader("Ocorrências Aeronáuticas 2010 - 2021")
st.write('''
O Centro de Investigação e Prevenção de Acidentes Aeronáuticos (CENIPA) é responsável pela gestão do banco de dados de ocorrências aeronáuticas. Este banco de dados engloba as ocorrências notificadas ao CENIPA entre os anos de 2010 e 2021, todas ocorridas em território brasileiro.
Dentre as informações disponíveis, destacam-se dados sobre as aeronaves envolvidas, ocorrências fatais, localização, data, horário dos eventos e informações taxonômicas comuns em investigações de acidentes (AIG). A privacidade das pessoas e entidades jurídicas envolvidas é preservada, conforme estipulado pela Lei de Acesso à Informação (Lei nº 12.527, de 18 de novembro de 2011).
Este banco de dados compreende informações preliminares provenientes do formulário CENIPA-05 (Formulário de Notificação de Ocorrências Aeronáuticas), além de dados consolidados a partir de relatórios de investigação publicados. Outra forma de acessar esses dados é por meio do Painel SIPAER, disponível no site do CENIPA.
Não estão incluídos neste banco de dados os dados dos Programas de Gerenciamento de Prevenção administrados pelo CENIPA (Emissão de Raio Laser e Risco de Balão). Esses programas possuem formulários de coleta de dados próprios, focados exclusivamente na gestão de riscos, enquanto os dados do formulário CENIPA-05 têm ênfase na investigação de acidentes (AIG).
    ''')

#Carregando os dados
df = load_data()

#Análise exploratória
exploratory_data_analysis(df)
