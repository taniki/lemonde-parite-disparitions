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
import datetime

import feedparser
import pandas as pd

# %%
source = 'https://www.lemonde.fr/disparitions/rss_full.xml'

# %%
disparitions_rss = feedparser.parse(source)

disparitions_rss.feed.keys()

# %%
df = pd.DataFrame.from_records(disparitions_rss.entries)

df.head()

# %%
today = datetime.datetime.today().strftime('%Y-%m-%d')

df.to_csv(f'daily_scrapping/{today}.csv', index=False)
