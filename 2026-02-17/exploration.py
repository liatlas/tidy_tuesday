# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %%
df = pd.read_csv("dataset.csv")
df.head()

# %%
df["measure"].unique()
# df[df["measure"].str.contains("Total")]["measure"].unique()

# %%
livestock = [
    "Total Sheep",
    "Total Dairy Cattle (including Bobby Calves)",
    "Total Beef Cattle",
    "Total Cattle",
    "Total Pigs",
    "Total goats",
    "Total Deer",
    "Total Ram and Wether Hoggets",
    "Total Sheep other than Ewes/Ewe Hoggets put to Ram"
]
fig, ax = plt.subplots(figsize = (10,10))
for animal in livestock:
    selected = df[(df['measure'] == animal) & (df['year_ended_june'] > 1970)]
    x = selected['year_ended_june']
    y = selected['value']
    ax.plot(x, y, label = animal)
ax.legend()

# %%
df[df['measure'].isin(livestock)].groupby('measure')['year_ended_june'].agg('min')

# %% 
df[df["measure"].str.contains("yield")]["measure"].unique()
# %%
ag_industries  = [
    'Wheat (yield)',
    'Barley (yield)',
    'Oats (yield',
    'Maize (yield)',
    'Seed/field peas (yield)'
]

fig, ax = plt.subplots(figsize = (16,8))
for industry in ag_industries:
    selected_industry = df[df['measure'] == industry]
    x = df['year_ended_june']
    y = df['value']
    ax.plot(x, y, label = industry)
ax.set_xticks(np.arange(1934, 2030, 5.0))
ax.legend()
fig.savefig('output.png')
