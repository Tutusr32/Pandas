# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

for i in pontos:
    filtro.append(i>=50)
filtro

 # %%

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado
# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32, 35, 14],
        "uf": ["sp", "pr", "rj"],     
     }
)

filtro = brinquedo["idade"] >= 18
brinquedo[filtro]

# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()


# %% Valores maiores que 50

filtro = df["QtdePontos"] >= 50
df[filtro]

# %% Pode usar * como um and    (Valores entre 50 e 100)

filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filtro]


# %% Pode usar + como um Or     (Valores == 1 ou == 100)

filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]

# %% pontos entre 0 e 50 ou do ano de 2025 para frente

filtro = ((df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50)) | (df["DtCriacao"] >= '2025-01-01')
df[filtro]

# %% 

True  and True  = True
True  and False = False
False and True  = False
False and False = False

True  or True  = True
True  or False = True
False or True  = True
False or False = False