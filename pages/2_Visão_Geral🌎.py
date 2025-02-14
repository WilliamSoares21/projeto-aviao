import streamlit as st

st.title("Visão Geral")

# Título da página
st.title("Gerenciamento de Riscos na Aviação")

# Introdução
st.header("Introdução")
st.write("""
No contexto da aviação, o gerenciamento de riscos é o processo mais importante para manter a segurança das operações em um nível aceitável.
O processo de gerenciamento de riscos compreende as seguintes fases:
""")

# Seções de gerenciamento de risco
st.header("Fases do Gerenciamento de Risco")
st.subheader("1. Identificar Perigos")
st.write("""
Perigo é uma condição, objeto ou atividade que potencialmente pode causar lesões às pessoas, danos a bens (equipamentos ou estruturas), perda de pessoal ou redução da habilidade para desempenhar uma função determinada.
""")

with st.expander("Exemplos de Perigos"):
  st.write("""
    - Fusões ou aquisições, no contexto organizacional
    - Falta de sinalização adequada
    - Aves próximas às áreas de pouso e decolagem de um aeródromo qualquer
    - Não cumprimento do checklist mínimo operacional ao iniciar a operação de uma aeronave
    - Falha de um rádio de comunicação
    - Instrumentos de medição ou ferramentas com deficiências de calibração
    - Falta de procedimento de passagem de serviço
    - Ambiente de trabalho barulhento
    """)

st.subheader("2. Avaliar as Consequências")
st.write("""
Para cada situação de perigo, você precisa ter clareza sobre o que tem potencial para causar danos. Isso ajudará você a identificar a melhor maneira de gerenciar o risco.
""")

st.subheader("3. Analisar o Risco")
st.write("""
Após identificadas as consequências, deve-se partir para o gerenciamento dos riscos.
""")

with st.expander("Definição de Risco"):
  st.write("""
    De maneira simples, podemos dizer que o termo “risco” se refere à chance de alguém ser prejudicado por vários perigos, juntamente com uma indicação de quão sérios podem ser os danos.
    """)

st.subheader("4. Desenvolver Estratégias de Mitigação")
st.write("""
Após ter identificado os perigos, avaliado as consequências e definido os níveis de risco, você deve fazer tudo o que for “razoavelmente praticável" para mitigar os riscos identificados.
""")

st.subheader("5. Implementar e Avaliar as Estratégias")
st.write("""
Depois de determinar os níveis de risco, avalie as defesas ou os controles estabelecidos para verificar a efetividade deles em relação ao perigo identificado.
""")

# Sistema de Relato
st.header("Sistema de Relato")
st.write("""
Um bom sistema de relato voluntário permite que qualquer pessoa reporte situações de perigo, real ou potencial, facilitando a identificação reativa e proativa dos perigos à segurança operacional.
""")

# Exemplo de Identificação e Avaliação de Perigos
st.header("Exemplo de Identificação e Avaliação de Perigos")
st.write("""
Perigo: A presença de objetos estranhos na pista de pouso e decolagem
Causas: A presença de objetos estranhos na pista de pouso e decolagem pode ser resultantes de:
- Falta de atenção do pessoal que atua em solo
- Danos na aeronave que provocaram a queda de algum item
- Sujeira e descuido nas áreas próximas à pista de pouso e decolagem
""")

# Conclusão
st.header("Conclusão")
st.write("""
O processo de gerenciamento da segurança operacional somente estará concluído quando a organização testar a validade de suas decisões e avaliar a efetividade das medidas mitigadoras implementadas.
""")
