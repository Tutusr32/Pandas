# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")

df.head()

# %%

def get_last_id(x):
    return x.split("-")[-1]

# %%

print(get_last_id("ff8d55dc-64fa-40de-992a-04a4155f5634"))

# %%

id_novo = []

for i in df["IdCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["Novo_id"] = id_novo
df.head()

# %%

df["IdCliente"] = df["IdCliente"].apply(get_last_id)

df
