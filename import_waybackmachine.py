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
import feedparser
import requests
from tqdm import tqdm

import glob

# %%
source = 'https://www.lemonde.fr/disparitions/rss_full.xml'

# %%
logs = pd.DataFrame(columns=['available'], index=pd.DatetimeIndex(pd.date_range('2014-04-07', '2022-08-01')))

logs

# %%
for d in tqdm(logs.index):
    date = d.strftime('%Y%m%d')
    
    res = requests.get(f'https://archive.org/wayback/available?url={source}&timestamp={date}')
    
    try:
        url = res.json()['archived_snapshots']['closest']['url']
        rss = feedparser.parse(url)
        tmp = pd.DataFrame.from_records(rss.entries)
        tmp.to_csv(f'backfill/{date}.csv', index=False)

        logs.loc[d,'available'] = True
    except:
        logs.loc[d,'available'] = False

# %%
logs

# %%
raw = pd.concat([pd.read_csv(f) for f in glob.glob('backfill/*.csv')])

raw.shape

# %%
articles = (raw
    .drop_duplicates(subset='id')
    [[
        'id',
        'published',
        'title',
        'summary'
    ]]
)

articles.shape

# %%
articles.to_csv('articles.backfill.csv', index=False)
