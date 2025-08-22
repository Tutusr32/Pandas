# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%

df["pontos_100"] = df["QtdePontos"] + 100
df.head()

# %%

nova_coluna = []
for i in df["QtdePontos"]:
    nova_coluna.append( i+100)

nova_coluna

# %%

df["EmailTwitch"] = df["FlEmail"] + df["FlTwitch"]
df.head()

# %%

df["Email&Twitch"] = df["FlEmail"] * df["FlTwitch"]
df.head()

# %%

df["QtdeSocial"] = df["FlEmail"] + df["FlTwitch"] + df["FlYouTube"] + df["FlBlueSky"] + df["FlInstagram"]
df

# %%

df["Todas_Socials"] = df["FlEmail"] * df["FlTwitch"] * df["FlYouTube"] * df["FlBlueSky"] * df["FlInstagram"]
df

# %%

df["QtdePontos"]

# %%

df["log_pontos"] = np.log(df["QtdePontos"].replace(0, np.nan))
df["log_pontos"].describe()

# %%

import matplotlib.pyplot as plt

plt.grid(True)
plt.hist(df["log_pontos"])
plt.show()
