import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Analise de riscos")
with st.container():
    st.subheader("Por que devemos gerenciar riscos?")
    st.write(
        "O gerenciamento de riscos tem como objetivo orientar a alocação equilibrada dos recursos para o controle racional dos riscos que afetam as operações de uma organização."
    )
    st.image(
        'https://www.pilotopolicial.com.br/wp-content/uploads/2013/03/gerenciamento2.jpg',
        caption='Gerencia de riscos by Piloto Policial')
    st.write(
        'Para decidir como e quando atravessar a rua, precisamos avaliar os perigos presentes nesse cenário (existência de carros em alta velocidade, inexistência de faixa de pedestre ou sinal de trânsito etc.)'
    )


def generate_alarp_chart(data):
    fig = go.Figure()

    # Adiciona barras para representar os riscos
    fig.add_trace(
        go.Bar(x=data["Categoria"],
               y=data["Risco"],
               name="Risco",
               marker_color=get_colors(data)))

    # Calcula o ALARP como a média dos riscos
    alarp = data["Risco"].mean()

    # Adiciona uma linha horizontal para representar o ALARP
    fig.add_shape(type="line",
                  x0=-0.5,
                  y0=alarp,
                  x1=len(data["Categoria"]) - 0.5,
                  y1=alarp,
                  line=dict(color="black", width=3, dash="dash"),
                  name="ALARP")

    fig.update_layout(title="Gráfico ALARP",
                      xaxis_title="Categoria",
                      yaxis_title="Risco",
                      barmode="group")
    return fig


def get_colors(data):
    colors = []
    for risco in data["Categoria"]:
        if risco == "Risco Inaceitável":
            colors.append("red")
        elif risco == "Risco Tolerável e Análise de Benefício/Custo":
            colors.append("yellow")
        elif risco == "Risco Aceitável":
            colors.append("green")
    return colors


def main():
    st.title("Registro de Perigo e Gráfico ALARP")

    # Entrada de dados do usuário
    categoria = st.selectbox("Categoria de Perigo:", [
        "Risco Inaceitável", "Risco Tolerável e Análise de Benefício/Custo",
        "Risco Aceitável"
    ])
    localizacao = st.text_input("Localização do Perigo:")
    consequencias = st.text_input("Consequências Potenciais:")
    risco = st.slider("Risco (1-10):", 1, 10)

    if st.button("Adicionar Perigo"):
        # Salva os dados em um DataFrame
        novo_perigo = pd.DataFrame({
            "Categoria": [categoria],
            "Localização": [localizacao],
            "Consequências": [consequencias],
            "Risco": [risco]
        })

        # Se o arquivo já existe, apenas adiciona o novo perigo
        try:
            perigos = pd.read_csv("perigos.csv")
            perigos = pd.concat([perigos, novo_perigo], ignore_index=True)
        except FileNotFoundError:
            perigos = novo_perigo

        # Salva os dados no arquivo CSV
        perigos.to_csv("perigos.csv", index=False)

        st.success("Perigo adicionado com sucesso!")

    # Carrega os dados dos perigos
    try:
        perigos = pd.read_csv("perigos.csv")
    except FileNotFoundError:
        perigos = pd.DataFrame(
            columns=["Categoria", "Localização", "Consequências", "Risco"])

    # Exibe os perigos registrados
    st.subheader("Perigos Registrados:")
    st.write(perigos)

    # Gera e exibe o gráfico ALARP
    st.subheader("Gráfico ALARP:")
    fig = generate_alarp_chart(perigos)
    st.plotly_chart(fig)


if __name__ == "__main__":
    main()
