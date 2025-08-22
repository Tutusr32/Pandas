# 📊 Estudos e Projetos em Pandas

Este repositório reúne **estudos e projetos práticos com a biblioteca Pandas** em Python, organizados de forma sequencial para aprendizado estruturado.  
Os conteúdos aqui cobrem desde conceitos básicos de Pandas até manipulação avançada de dados e integração com SQL.  

Durante o curso, utilizaremos **dados reais**, fornecidos pelo [Teo Me Why](https://www.kaggle.com/datasets/teocalvo/teomewhy-loyalty-system).  

---

## 🚀 Conteúdo estudado

### 1. Principais objetos do Pandas
- **Series** → estrutura unidimensional, útil para listas e vetores.  
- **DataFrames** → estrutura bidimensional, ideal para tabelas e planilhas.

### 2. Importando arquivos com Pandas
- Leitura de arquivos: `csv`, `xlsx` e `parquet`.  
- Manipulação básica de dados importados.

### 3. Navegando pelos dados
- Obter informações básicas sobre DataFrames (`info()`, `describe()`).  
- Conhecer tipos de colunas e tipos de dados.  
- Seleção e navegação em linhas e colunas (`loc`, `iloc`).  
- Renomear colunas de forma prática e padronizada.

### 4. Filtrando dados
- Aplicação de **condições lógicas** para filtrar linhas.  
- Combinação de múltiplas condições.

### 5. Transformações e remoções
- Criação de **novas colunas** derivadas de existentes.  
- Ordenação de dados por valores de colunas.  
- Conversão de tipos (`astype`, `to_datetime`, etc.).  
- Aplicação de funções em linhas e colunas (`apply`).  
- Remoção de duplicatas (`drop_duplicates`).  
- Tratamento de valores ausentes (`fillna`, `dropna`).

### 6. GroupBy
- **Agregação de dados** para sumarizar informações.  
- Uso do método `agg` para múltiplas operações.  
- Criação de **agregações personalizadas** para análises mais complexas.

### 7. Cruzamento de dados
- Combinação de DataFrames com **`merge`** (inner, left, right, outer).  
- Concatenação de dados vertical ou horizontalmente com **`concat`**.

### 8. Conectando com Bancos SQL
- Importação de dados de bancos SQL usando **SQLAlchemy**.  
- Execução de queries dentro do Python.  
- Escrita de DataFrames de volta para o banco.

---

## 💡 Dataset utilizado

Utilizaremos dados reais durante os estudos:  
**[Loyalty System Dataset - Teo Me Why](https://www.kaggle.com/datasets/teocalvo/teomewhy-loyalty-system)**

> ⚠️ Créditos ao **Teo Me Why** pelo dataset e licença de uso.

---

## 🛠️ Bibliotecas utilizadas
- **Pandas** → manipulação e análise de dados  
- **NumPy** → cálculos e operações numéricas  
- **Matplotlib** → visualização de dados  
- **SQLAlchemy** → conexão e manipulação de bancos SQL  
- **Scikit-Learn** → preparação para Machine Learning  


---

## 💡 Como usar

1. Clone o repositório:
```bash
git clone https://github.com/Tutusr32/Pandas.git
cd Pandas
```

Não esqueça de baixar os dados!
