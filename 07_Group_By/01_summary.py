# %%

import pandas as pd

idades = [32,44,12,54,67,32,23,34,32,12,45,43,28,73,29]
idades = pd.Series(idades)
idades

idades.sum()
idades.min()
idades.max()
idades.mean()
idades.describe()

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%

clientes["FlTwitch"].sum()
clientes["FlTwitch"].mean()

# %%

redes_sociais = ["FlEmail", "FlTwitch", "FlYouTube", "FlBlueSky", "FlInstagram"]
clientes[redes_sociais].sum()

# %%

num_coluns = clientes.dtypes[~(clientes.dtypes == "object")].index.tolist()
clientes[num_coluns].mean()

# %%

clientes[num_coluns].describe()

# %%

clientes[["FlTwitch", "FlEmail"]].describe()
