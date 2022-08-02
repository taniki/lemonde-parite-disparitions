# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

# %%
source = 'https://docs.google.com/spreadsheets/d/1UgWS00I_U_9B4A2M8okPAix_kIJz6TP-zObpOeV3pMM/gviz/tq?tqx=out:csv&sheet=gendered'

# %%
articles_gendered = pd.read_csv(source)

# %%
people = (articles_gendered
    .drop_duplicates(subset='entity')
    [['entity', 'gender']]
    .reset_index(drop=True)
)

people

# %%
people.to_csv('people.csv', index=False)
