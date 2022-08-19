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
import glob
import os

# %%
raw = pd.concat([pd.read_csv(f) for f in glob.glob('daily_scrapping/*.csv')])

raw.shape

# %%
raw.head(1).T

# %%
articles = (raw
    .drop_duplicates(subset='id')
    [[
        'id',
        'published',
        'title',
        'summary'
    ]]
    .assign(
        date = lambda df: pd.to_datetime(df.published)
    )
    .sort_values('date', ascending=False)
    .drop('date', axis=1)
)

articles

# %%
articles.to_csv('articles.csv', index=False)
