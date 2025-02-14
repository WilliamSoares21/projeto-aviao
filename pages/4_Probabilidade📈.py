import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuração do título e descrição da página
st.title("Análise de Probabilidade na Aviação")

st.write("""
    Na gestão de riscos na aviação, a análise de probabilidade desempenha um papel crucial na avaliação e mitigação dos perigos associados às operações aéreas. Compreender a probabilidade de ocorrência de eventos adversos é essencial para priorizar recursos e implementar medidas preventivas adequadas.

    Uma maneira de determinar a probabilidade de um evento é considerar a frequência potencial de sua ocorrência com base na exposição ao perigo. Por exemplo, o risco de um evento pode ser maior em operações de aeronaves com voos diários em comparação com aquelas com voos semanais.

    Uma abordagem comum para avaliar a probabilidade é utilizar uma escala simples de cinco pontos, onde cada categoria representa um nível diferente de probabilidade. Esta escala pode variar de "Extremamente improvável" a "Frequente", com valores numéricos atribuídos a cada categoria para quantificar a probabilidade. Por exemplo, um carregamento incorreto de aeronaves, uma atividade regular na aviação, pode ser avaliado como "Ocasional" na escala de probabilidade, indicando que o evento ocorre algumas vezes, mas não com frequência significativa.

    É importante ressaltar que cada operador pode adaptar essa escala de probabilidade de acordo com as especificidades de suas operações. Registrar as tabelas e metodologias utilizadas para avaliação de riscos no Manual de Gerenciamento da Segurança Operacional é essencial para garantir uma abordagem consistente e documentada na gestão de riscos na aviação.

    Em resumo, a análise de probabilidade fornece uma estrutura sistemática para avaliar e quantificar o risco na aviação, permitindo que as organizações identifiquem, priorizem e mitiguem eficazmente os perigos associados às suas operações aéreas.
    """)

# Seção de introdução
st.header("Introdução")
st.write("""
Uma tarefa importante na análise do risco é determinar o nível de risco com base em sua probabilidade de acontecer. 
O risco pode ser avaliado considerando a probabilidade de um evento ocorrer com base na exposição ao perigo. 
Por exemplo, se o perigo está associado a uma operação de uma aeronave com voos diários, a probabilidade de ter uma consequência 
é maior do que aquela aeronave que tem apenas um voo semanal. Uma maneira simples de determinar a probabilidade é classificar o risco 
com base em sua frequência potencial de ocorrência. Isso pode ser feito em uma escala simples de cinco pontos, que varia, por exemplo, 
de probabilidade rara a muito provável de ocorrer.
""")

# Seção de avaliação de risco
st.header("Avaliação de Risco")
st.subheader("Probabilidade e Severidade")

# Tabela de categorias de probabilidade
dados = {
    'Categoria': [
        'Frequente', 'Ocasional', 'Remoto', 'Improvável',
        'Extremamente improvável'
    ],
    'Significado': [
        'É provável que ocorra muitas vezes (tem ocorrido frequentemente)',
        'É provável que ocorra o evento algumas vezes (tem ocorrido com pouca frequência)',
        'Improvável que ocorra o evento, mas é possível que venha a ocorrer (ocorre raramente)',
        'Bastante improvável que o evento ocorra (não se tem notícia de que tenha ocorrido)',
        'Quase impossível que o evento ocorra'
    ],
    'Valor': [5, 4, 3, 2, 1]
}
df_probabilidade = pd.DataFrame(dados)
st.write(df_probabilidade)

# Entradas para o usuário adicionar dados de probabilidade e severidade
st.subheader("Adicionar Dados de Probabilidade e Severidade")
probabilidade = st.selectbox("Selecione a probabilidade:", [
    "Frequente", "Ocasional", "Remoto", "Improvável",
    "Extremamente improvável"
])
severidade = st.selectbox(
    "Selecione a severidade:",
    ["Catastrófica", "Crítica", "Significativa", "Pequena", "Insignificante"])
valor = st.number_input("Valor de Risco (1-5):", 1, 5, 1)

# Função para salvar dados no arquivo CSV
def save_to_csv(data):
    file_path = "user_data.csv"
    df = pd.DataFrame(data)
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)

# Armazenando dados inseridos pelo usuário
if "user_data" not in st.session_state:
    st.session_state["user_data"] = {
        "Probabilidade": [],
        "Severidade": [],
        "Valor": []
    }

if st.button("Adicionar Dados"):
    st.session_state["user_data"]["Probabilidade"].append(probabilidade)
    st.session_state["user_data"]["Severidade"].append(severidade)
    st.session_state["user_data"]["Valor"].append(valor)
    save_to_csv(st.session_state["user_data"])
    st.success("Dados adicionados com sucesso!")

# Convertendo dados do usuário para DataFrame
user_data_df = pd.DataFrame(st.session_state["user_data"])

# Exibir dados do usuário
if not user_data_df.empty:
    st.subheader("Dados de Usuário")
    st.write(user_data_df)

# Gráfico interativo para demonstrar a distribuição de riscos com base na probabilidade e severidade
st.subheader("Distribuição de Riscos")
if not user_data_df.empty:
    # Gráfico de barras empilhadas
    fig = px.bar(user_data_df,
                 x='Probabilidade',
                 y='Valor',
                 color='Severidade',
                 title='Distribuição de Riscos com Dados do Usuário',
                 labels={'Valor': 'Nível de Risco'},
                 text='Valor')

    fig.update_layout(barmode='stack')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("Insira os dados para visualizar a distribuição de riscos.")

# Widget para entrada de dados para avaliação de risco
st.subheader("Avaliação de Risco Personalizada")
probabilidade = st.selectbox("Selecione a probabilidade para avaliação personalizada:", [
    "Frequente", "Ocasional", "Remoto", "Improvável",
    "Extremamente improvável"
])
severidade = st.selectbox(
    "Selecione a severidade para avaliação personalizada:",
    ["Catastrófica", "Crítica", "Significativa", "Pequena", "Insignificante"])
nota_risco = st.slider("Nota de Risco (1-5):", 1, 5)

# Função para calcular o valor de risco
def calcular_valor_risco(prob, sev, nota):
    valor_prob = df_probabilidade.loc[df_probabilidade['Categoria'] == prob, 'Valor']
    if not valor_prob.empty:
        valor_prob = valor_prob.values[0]
    else:
        valor_prob = 0
    valor_sev = {
        "Catastrófica": 5,
        "Crítica": 4,
        "Significativa": 3,
        "Pequena": 2,
        "Insignificante": 1
    }[sev]
    return valor_prob * valor_sev * nota

valor_risco = calcular_valor_risco(probabilidade, severidade, nota_risco)

st.write("### Resultado da Avaliação de Risco Personalizada")
st.write(f"**Probabilidade selecionada:** {probabilidade}")
st.write(f"**Severidade selecionada:** {severidade}")
st.write(f"**Nota de Risco:** {nota_risco}")
st.write(f"**Valor de Risco Calculado:** {valor_risco}")

# Seção de gestão de riscos
st.header("Gestão de Riscos")
st.subheader("Mitigação de Riscos")
st.write("Estratégias para mitigar riscos na aviação.")

# Incluindo sugestões de mitigação de riscos e sobre como lidar com eles.
mitigacao = {
    "Estratégia": [
        "Eliminação", "Substituição", "Controles de Engenharia",
        "Controles Administrativos", "Equipamento de Proteção Individual (EPI)"
    ],
    "Descrição": [
        "Remover o risco completamente.",
        "Substituir o perigo por algo menos perigoso.",
        "Projetar controles físicos para reduzir a exposição.",
        "Implementar políticas e procedimentos para reduzir o risco.",
        "Usar EPIs para proteger contra os riscos residuais."
    ]
}
df_mitigacao = pd.DataFrame(mitigacao)
st.write(df_mitigacao)

# Seção de conclusão
st.header("Conclusão")
st.write("""
A gestão eficaz de riscos na aviação é essencial para garantir a segurança de todos os envolvidos. 
Ao entender e avaliar os riscos corretamente, é possível implementar estratégias eficazes para mitigá-los.
""")
