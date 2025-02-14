# Projeto - Gestão de Riscos na Aviação

Projeto sobre gestão de riscos na área de aviação (projeto extensionista ESTACIO, disciplina Big Data com Python). O projeto foi **finalizado e apresentado no final do primeiro semestre de 2024**. 

---

## 📌 Descrição do Projeto

Este projeto é um **aplicativo web interativo** desenvolvido com **Streamlit**, focado no gerenciamento de riscos na aviação. Ele utiliza diversas bibliotecas como **pandas**, **plotly** e **numpy** para manipulação de dados e visualização.

🔹 Aqui está uma visão geral das principais funcionalidades:

## 🚀 Funcionalidades Principais

### 🏷️ Configuração da Página:

- O título da página é configurado para **"Meu site usando o Streamlit"**.

### 📖 Introdução ao Gerenciamento de Riscos:

- A página inicial contém um título e uma breve explicação sobre a **importância do gerenciamento de riscos na aviação**.

### 📊 Matriz de Tolerância para Avaliação de Risco:

- Uma função `gerar_matriz_tolerancia` gera uma matriz de tolerância para avaliação de risco, mapeando **categorias de risco para cores específicas**.
- A matriz é exibida como um **DataFrame estilizado** com cores representando diferentes níveis de risco.

### 🔍 Seleção de Categoria de Risco:

- Um **selectbox** permite ao usuário selecionar uma categoria de risco (**Catastrófico, Crítica, Significativa, Pequena, Insignificativa**).
- Dependendo da seleção, uma descrição detalhada da categoria de risco é exibida usando `st.markdown`.

### 📈 Matriz de Risco Interativa:

- Uma função `gerar_matriz_risco_interativa` cria uma matriz de risco **interativa** usando **Plotly**.
- A matriz é exibida como um **gráfico interativo** na página.

### 📅 Geração de Dados Fictícios:

- Uma função `gera_dados_mes` gera **dados fictícios** para um mês específico, que podem ser usados para **simulações** ou **análises**.

### 🗂️ Sidebar com Informações Adicionais:

- A **sidebar** contém uma **imagem e uma legenda** para as classificações de riscos, com **cores correspondentes** a cada nível de risco.

---

## 🏗️ Estrutura do Código

O código está organizado em várias seções, cada uma responsável por uma parte específica da funcionalidade do aplicativo:

📌 **Importações:** Importa as bibliotecas necessárias (`streamlit`, `pandas`, `plotly.express`, `numpy`).

📌 **Configuração da Página:** Define o título da página.

📌 **Conteúdo Principal:** Contém a introdução e a explicação sobre o gerenciamento de riscos.


📌 **Funções:**

- `gerar_matriz_tolerancia`: Gera a matriz de tolerância e mapeia as cores.
- `gera_dados_mes`: Gera dados fictícios para um mês específico.
- `gerar_matriz_risco_interativa`: Cria uma matriz de risco interativa usando **Plotly**.
  📌 **Exibição de Dados:** Exibe a matriz de tolerância e a matriz de risco interativa.
  📌 **Sidebar:** Exibe informações adicionais e uma legenda para as classificações de riscos.

---

## ▶️ Exemplo de Uso

Para executar o aplicativo, utilize o seguinte comando no terminal:

```sh
streamlit run main.py
```

Isso iniciará o aplicativo **Streamlit** e abrirá uma **interface web interativa** para explorar as funcionalidades mencionadas acima.

---

## 📚 Fontes e Referências

Os dados utilizados no projeto foram obtidos do **Kaggle**, através do seguinte conjunto de dados: [OpenDataAIGBrazil](https://www.kaggle.com/datasets/nosbielcs/opendataaigbrazil).

📌 O usuário responsável pela publicação dos dados no Kaggle é **[nosbielcs](https://github.com/nosbielcs?tab=overview\&from=2025-02-01\&to=2025-02-14)**.

---

💡 **Projeto finalizado e documentado! Obrigado por conferir!** 🚀


