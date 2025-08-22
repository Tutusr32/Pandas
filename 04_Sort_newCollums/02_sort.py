# %% 

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

max_ponto = clientes["QtdePontos"].max()
filtro = clientes["QtdePontos"] == max_ponto
clientes[filtro]

# %%

top_5 = (clientes.sort_values(by="QtdePontos", ascending=False).head(5)["IdCliente"])

type(top_5)

# %%

clientes

# %%

brinquedo = pd.DataFrame(
    {
        "Nome": ["Teo", "Ana", "Nah", "José"],
        "Idade": [32, 43, 35, 42],
        "Salário":[2345, 4533, 3245, 4533],
    }
)

brinquedo

# %%

brinquedo.sort_values(by=["Salário", "Idade"], ascending=[False, True])
