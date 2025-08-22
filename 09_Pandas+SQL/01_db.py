# %%

import pandas as pd
import sqlalchemy
from sqlalchemy import inspect

# %%

engine = sqlalchemy.create_engine("sqlite:///../Data/database.db")

insp = inspect(engine)
print(insp.get_table_names())

# %%

clientes = pd.read_sql_table(table_name="clientes", con=engine)

# %%

clientes.shape

# %%

query = "SELECT * FROM clientes LIMIT 100"

df_100 = pd.read_sql_query(query, con=engine)
df_100
