# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%

df.shape

# %%

df.info(memory_usage='deep')

# %%

df.dtypes

# %%
renamed_coluns = {"QtdePontos": "QTPontos",
                         "DescSistemaOrigem": "SistemaOrigem"}

df.rename(columns=renamed_coluns, inplace=True)

# %%

df

# %%

colunas = ["IdCliente", "QTPontos"]
df[colunas]

# %%

df

# %%
# SELECT idCliente FROM df

df[["IdCliente"]]

# %%

# SELECT idCliente, qtPontos FROM df LIMIT 5
df[["IdCliente", "QTPontos"]].tail(5)

# %%

# SELECT idCliente, idTransacao, qtPontos
# FROM df
# LIMIT 5

df[["IdCliente", "IdTransacao", "QTPontos"]].head(5)

# %%

colunas = list(df.columns)
colunas.sort()
colunas

df = df[colunas]
df
