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
import spacy
import pandas as pd
import polars as pl

# %%
df = pd.read_csv('articles.backfill.csv')

# %%
nlp = spacy.load('fr_core_news_sm')

# %%
df

# %%
test = (df
    .sample(1)
    [['title', 'summary']]
)

test

# %%
doc = nlp(test['title'].iloc[0] +' ' +test['summary'].iloc[0])

# %%
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


# %%
def find_people(txt : str):
    return [ ent.text for ent in (nlp(str(txt))).ents if ent.label_ == 'PER' ]

# docs = (df.with_columns(
#     [
#         pl
#             .apply(lambda d: find_people(d['title']))
#             .first()
#             .alias('title_detect')
#     ]
# )
        
# )
        
docs = (df
    [['title', 'summary']]
    .assign(
        title_detect = lambda d: d['title'].apply(find_people),
        summary_detect = lambda d: d['summary'].apply(find_people)
    )
)

docs

# %%
docs[ (docs['title_detect'].apply(lambda x: len(x)) == 0) * (docs['summary_detect'].apply(lambda x: len(x)) == 0) ]


# %%
def first(row):
    if len(row['title_detect'] + row['summary_detect']) > 0:
        return list(row['title_detect'] + row['summary_detect'])[0]
    else:
        return ''

firsts = docs.apply(first , axis=1)

# %%
