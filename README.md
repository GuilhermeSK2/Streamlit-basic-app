# Aplicativo simples usando Streamlit

Este projeto contém um aplicativo web simples construído com Streamlit, uma biblioteca Python que permite criar interfaces de usuário interativas para análise de dados e machine learning de forma rápida. O objetivo é demonstrar as funcionalidades básicas e o potencial do Streamlit para transformar scripts Python em aplicações web amigáveis.

## Visão Geral

O aplicativo `app.py` é um exemplo didático que mostra como:
* Exibir diferentes tipos de texto (títulos, cabeçalhos, subcabeçalhos, markdown).
* Trabalhar com dados tabulares usando DataFrames do Pandas.
* Criar gráficos simples com Matplotlib.
* Adicionar widgets interativos, como botões, sliders e caixas de seleção.
* Implementar layouts de interface com colunas e barra lateral.
* Carregar e filtrar dados de um arquivo CSV.

## Estrutura do Projeto

* `app.py`: O script principal do aplicativo Streamlit.
* `funcionarios.csv`: Um arquivo CSV de exemplo contendo dados para demonstração de carregamento e filtragem.

## Tecnologias Utilizadas

* **Python 3**
* **Streamlit**: A principal biblioteca para criar a aplicação web.
* **Pandas**: Para manipulação e análise de dados.
* **Matplotlib**: Para criação de gráficos.

## Pré-requisitos

Para executar este projeto, você precisará ter o Python instalado. É altamente recomendado usar um ambiente virtual.

## Funcionalidades Demonstradas

O aplicativo exibirá uma série de elementos e interações, incluindo:

* **Títulos e Textos:** `st.title`, `st.header`, `st.subheader`, `st.text`, `st.markdown`.
* **DataFrames:** `st.dataframe` para tabelas interativas e `st.table` para tabelas estáticas.
* **Gráficos:** Um gráfico de barras simples gerado com `matplotlib` e exibido com `st.pyplot`.
* **Botões:** Um botão que exibe uma mensagem ao ser clicado (`st.button`).
* **Sliders:** Um slider para selecionar um valor numérico (`st.slider`).
* **Caixas de Seleção:** Uma `selectbox` para escolher uma opção de uma lista (`st.selectbox`).
* **Carregamento e Filtragem de Dados:** Exemplo de como carregar um CSV e filtrar dados interativamente com um slider de idade.
* **Layouts:** Uso de `st.columns` para dividir o conteúdo em colunas e `st.sidebar` para criar filtros na barra lateral.
