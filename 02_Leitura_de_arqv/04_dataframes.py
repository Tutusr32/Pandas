# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes

# %% Cabeçalho, 10 primeiros

df_clientes.head(10)

# %% Últimos 5

df_clientes.tail(5)

# %% 10 aleatórios

df_clientes.sample(10)

# %% Número de linhas e colunas

df_clientes.shape

# %% Nome das colunas

df_clientes.columns

# %% Índices da tabela

df_clientes.index

# %% Informações

df_clientes.info(memory_usage="deep", max_cols = 2)

# %% Série que diz valores de cada coluna

df_clientes.dtypes
