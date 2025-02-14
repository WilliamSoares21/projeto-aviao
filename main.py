import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Meu site usando o Streamlit")

with st.container():
    st.title("Gerenciamento de Riscos da Aviação")
    st.write(
        "É de suma importância para quem trabalha com aviação como as questões que envolvem risco são importantes, e que devem ser tratadas, logo abaixo você pode ver uma simulação de uma matriz de riscos."
    )


# Função para gerar a matriz de tolerância para avaliação de risco
@st.cache_data
def gerar_matriz_tolerancia():
    matriz_tolerancia = [['5A', '5B', '5C', '5D', '5E'],
                         ['4A', '4B', '4C', '4D', '4E'],
                         ['3A', '3B', '3C', '3D', '3E'],
                         ['2A', '2B', '2C', '2D', '2E'],
                         ['1A', '1B', '1C', '1D', '1E']]

    mapeamento_cores = {
        '5A': '#FF5733',
        '5B': '#FF5733',
        '5C': '#FFC300',
        '5D': '#4CAF50',
        '5E': '#3498DB',
        '4A': '#FF5733',
        '4B': '#FFC300',
        '4C': '#FFC300',
        '4D': '#4CAF50',
        '4E': '#3498DB',
        '3A': '#FF5733',
        '3B': '#FFC300',
        '3C': '#4CAF50',
        '3D': '#3498DB',
        '3E': '#3498DB',
        '2A': '#FFC300',
        '2B': '#4CAF50',
        '2C': '#4CAF50',
        '2D': '#3498DB',
        '2E': '#BDC3C7',
        '1A': '#4CAF50',
        '1B': '#4CAF50',
        '1C': '#3498DB',
        '1D': '#3498DB',
        '1E': '#BDC3C7'
    }

    df_tolerancia = pd.DataFrame(
        matriz_tolerancia,
        index=[
            'Frequente', 'Provável', 'Remota', 'Extremamente Remoto',
            'Extremamente Improvável'
        ],
        columns=['Catastrófico', 'Perigoso', 'Maior', 'Menor', 'Desprezível'])

    df_tolerancia_cores = df_tolerancia.apply(
        lambda x: x.map(mapeamento_cores))
    return df_tolerancia, df_tolerancia_cores, mapeamento_cores


# Seção para mostrar a matriz de tolerância
with st.container():
    st.title("Análise de Gerenciamento de Riscos na Aviação")

    risco_opcao = st.selectbox("Selecione a categoria de risco:",
                               ("Catastrófico", "Crítica", "Significativa",
                                "Pequena", "Insignificativa"))

    if risco_opcao == "Catastrófico":
        st.markdown(
            "<span style='color: #FF5733;'>Catastrófico: Destruição dos equipamentos; múltiplas mortes</span>",
            unsafe_allow_html=True)
    elif risco_opcao == "Crítica":
        st.markdown(
            "<span style='color: #FFC300;'>Crítica: Uma redução importante das margens de segurança operacional, dano físico ou uma carga de trabalho tal que os operadores não podem desempenhar suas tarefas de forma precisa e completa; Lesões sérias; Graves danos ao equipamento.</span>",
            unsafe_allow_html=True)
    elif risco_opcao == "Significativa":
        st.markdown(
            "<span style='color: #4CAF50;'>Significativa: Uma redução significativa das margens de segurança operacional, uma redução na habilidade do operador em responder a condições operacionais adversas como resultado do aumento da carga de trabalho ou como resultado de condições que impedem sua eficiência; Incidente sério; Lesões às pessoas.</span>",
            unsafe_allow_html=True)
    elif risco_opcao == "Pequena":
        st.markdown(
            "<span style='color: #3498DB;'>Pequena: Interferência; Limitações operacionais; Utilização de procedimentos de emergência;Incidentes menores</span>",
            unsafe_allow_html=True)
    elif risco_opcao == "Insignificativa":
        st.markdown(
            "<span style='color: #BDC3C7;'>Insignificativa: Consequências leves.</span>",
            unsafe_allow_html=True)

    df_tolerancia, matriz_tolerancia_cores, mapeamento_cores = gerar_matriz_tolerancia(
    )
    st.subheader("Matriz de Tolerância para Avaliação de Risco: ")
    st.dataframe(
        matriz_tolerancia_cores.style.map(
            lambda x: f'background-color: {x}', subset=pd.IndexSlice[:, :]))


# Função para gerar dados fictícios para um mês em específico
@st.cache_data
def gera_dados_mes(mes):
    np.random.seed(
        42) # Para garantir que os resultados sejam os mesmos a cada execução

    dias = np.arange(1, 31)
    dados = np.random.randint(1, 100, size=len(dias))
    df = pd.DataFrame({'Dia': dias, 'Dados': dados})
    df['Mês'] = mes
    return df


# Criando o nome do projeto e a sidebar
st.sidebar.image(
    'https://www.fazenda.niteroi.rj.gov.br/blog/wp-content/uploads/2023/01/banner-Gestao-de-Riscos-.jpg',
    use_container_width=True)
st.sidebar.header('Gestão de riscos para aviação `Versão de Teste`')

# Exibindo uma legenda para as classificações de riscos
with st.sidebar:
    st.sidebar.header('Classificação de Riscos')
    st.subheader('Níveis de Riscos:')
    for label, color in {
            'Catastrófica': '#FF5733',  # Laranja
            'Crítica': '#FFC300',  # Amarelo
            'Significativa': '#4CAF50',  # Verde
            'Pequena': '#3498DB',  # Azul
            'Insignificante': '#BDC3C7'  # Cinza
    }.items():
        st.markdown(f'<span style="color:{color};">■</span> {label}',
                    unsafe_allow_html=True)


# Função para gerar a matriz de risco interativa com Plotly
def gerar_matriz_risco_interativa(df_tolerancia, mapeamento_cores):
    fig = px.imshow(
        df_tolerancia.map(lambda x: x[0]),
        labels=dict(x="Severidade", y="Probabilidade"),
        x=['Catastrófico', 'Perigoso', 'Maior', 'Menor', 'Desprezível'],
        y=[
            'Frequente', 'Provável', 'Remota', 'Extremamente Remoto',
            'Extremamente Improvável'
        ],
        color_continuous_scale=[
            mapeamento_cores['5A'], mapeamento_cores['4A'],
            mapeamento_cores['3A'], mapeamento_cores['2A'],
            mapeamento_cores['1A']
        ])
    return fig


# Seção para mostrar a matriz de risco interativa
with st.container():
    st.subheader("Matriz de Risco Interativa: ")
    fig = gerar_matriz_risco_interativa(df_tolerancia, mapeamento_cores)
    st.plotly_chart(fig, use_container_width=True)
