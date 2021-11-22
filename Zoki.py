import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
import pickle
import requests
from bs4 import BeautifulSoup
import json
from sqlalchemy import create_engine
import seaborn as sns
pd.options.mode.chained_assignment = None
y = pd.read_csv("all_games.csv")
y.drop('summary', axis=1, inplace=True)
y2 = y.iloc[0:1000]
print(y.isnull().sum())
print(y2.head())
print(y2.shape)
print(y["user_review"].value_counts())
print(y[y["user_review"] == "tbd"])
y = y.drop(y[y["user_review"] == "tbd"].index)
y["user_review"] = pd.to_numeric(y["user_review"])
print(y.dtypes)
nintendo = y[y["platform"].str.contains("Switch") + y["platform"].str.contains("Nintendo") + y["platform"].str.contains("Gamecube")
            + y["platform"].str.contains("Wii") + y["platform"].str.contains("DS") + y["platform"].str.contains("3DS") + y["platform"].str.contains("Game Boy Advance")]
nintendo = nintendo.reset_index()
nintendo.loc[:,'Company'] = "Nintendo"
nintendo = nintendo.iloc[0:100]
sony = y[y["platform"].str.contains("PlayStation") + y["platform"].str.contains("PSP")]
sony = sony.reset_index()
sony.loc[:,"Company"] = "Sony"
sony = sony.iloc[0:100]
microsoft = (y[y["platform"].str.contains("Xbox")]).reset_index()
microsoft.loc[:,"Company"] = "Microsoft"
microsoft = microsoft.iloc[0:100]
print(nintendo)
print(sony)
print(microsoft)
dtfs = [nintendo, sony, microsoft]
df = pd.concat(dtfs)
print(df.shape)
df = df.reset_index()
del df["level_0"]
del df["index"]
print(df.value_counts())
df["release_date"] = pd.to_datetime(df["release_date"])
df["release_year"] = df["release_date"].dt.year
print(df.head())
conditions = [
    (df['meta_score'] > 90) & (df['user_review'] > 9),
    (df['meta_score'] <= 90) & (df['user_review'] <= 9),
    (df['meta_score'] > 90) & (df['user_review'] <= 9),
    (df['meta_score'] <= 90) & (df['user_review'] > 9)
    ]
val= ["yes", "no", "no", "no"]
df["great_game"] = np.select(conditions, val)
print(df.value_counts("great_game"))
great_game = df[df["great_game"].str.contains("yes")]
sns.countplot(data=great_game, x="great_game", hue="Company")
plt.show()
g1 = sns.lineplot(x="release_year", y="meta_score", data=df, hue="Company", ci=None)
g1.set(xticks=df.release_year)
plt.xticks(rotation=90)
plt.show()
sns.catplot(x="Company", y="meta_score", data=df, kind="point", ci=None)
plt.show()
sns.catplot(x="Company", y="user_review", data=df, kind="point", ci=None)
plt.show()
sns.lineplot(data=df, x="release_year", y="user_review", hue="Company", ci=None)
plt.show()

def times10(x):
    return x * 10


df["burek"] = (df["user_review"]).apply(times10)
print(df["burek"])









