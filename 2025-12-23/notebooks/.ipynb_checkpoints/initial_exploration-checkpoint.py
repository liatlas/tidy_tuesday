# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
endangered_status_path = "../data/endangered_status.csv"
families_path = "../data/families.csv"
languages_path = "../data/languages.csv"

# %%
endangered_df = pd.read_csv(endangered_status_path)
families_df = pd.read_csv(families_path)
languages_df = pd.read_csv(languages_path)

# %%
endangered_df.head()

# %%
families_df.head()

# %%
languages_df.head()

# %%
languages_df[family_id] = 

