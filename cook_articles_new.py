# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

# %%
articles = pd.read_csv('articles.csv')

articles

# %%
source = 'https://docs.google.com/spreadsheets/d/1UgWS00I_U_9B4A2M8okPAix_kIJz6TP-zObpOeV3pMM/gviz/tq?tqx=out:csv&sheet=gendered'

# %%
articles_gendered = pd.read_csv(source)

articles_gendered

# %%
articles_new = articles[ ~articles.id.isin(articles_gendered.id.to_list()) ]

articles_new

# %%
articles_new.to_csv('articles.new.csv')
