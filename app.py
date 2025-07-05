import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Hello, Streamlit!")
st.write("Esse é meu primeiro app com Streamlit.")

st.header("Este é um Header")
st.subheader("Este é um Subheader")
st.text("Este é um texto simples.")
st.markdown("**Este é um texto em negrito.**")

# Dados
data = {
    "nome": ["Ana", "Bruno", "Carlos"],
    "idade": [23, 35, 45],
    "salario": [5000, 7000, 9000]
}

# Cria um DataFrame a partir dos dados
df = pd.DataFrame(data)
st.dataframe(df) # Exibe o DataFrame como uma tabela interativa
st.table(df)  # Exibe o DataFrame como uma tabela estática

# Exemplo de gráfico com matplotlib
fig, ax = plt.subplots()
ax.bar(df['nome'], df['salario'])
st.pyplot(fig)  # Exibe o gráfico matplotlib

#Exemplo de botão
if st.button("Clique aqui!"):
    st.write("Você clicou no botão!")

#Exemplo de slider
idade = st.slider("Selecione sua idade:", 0, 100, 25)
st.write(f"Idade selecionada: {idade}")


# Exemplo de seleção de opções com selectbox
opcao = st.selectbox(
    "Escolha um departamento:", 
    ["Recursos Humanos", "TI", "Vendas"])

st.write(f"Departamento selecionado: {opcao}")



#Carregando um arquivo CSV e filtrando dados

df = pd.read_csv("funcionarios.csv")

st.dataframe(df)

idade_min = st.slider("Idade mínima:", 0, 100, 30)
df_filtrado = df[df['idade'] > idade_min]
st.dataframe(df_filtrado)

# Exemplo de layout com colunas
col1, col2 = st.columns(2)

with col1:
    st.header("Coluna 1")
    st.write("Conteúdo da coluna 1")

with col2:
    st.header("Coluna 2")
    st.write("Conteúdo da coluna 2")


# Filtros na barra lateral
st.sidebar.header("Filtros")
idade_min = st.sidebar.slider("Idade mínima:", 0, 100, 30)