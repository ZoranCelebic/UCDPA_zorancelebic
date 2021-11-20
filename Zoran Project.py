#import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import dataset

raw_df = pd.read_csv("all_games.csv")

#checking for shape and missing data

print(raw_df.head())
print(raw_df.shape)
print(raw_df.isnull().sum())
#delete summary column

del raw_df["summary"]

#checking for data types

print(raw_df.dtypes)

#user review should be float

print(raw_df["user_review"].value_counts())

#drop tbd so we can change column type from object to float (first tbd game in place 679)

print(raw_df[raw_df["user_review"] == "tbd"])
raw_df = raw_df.drop(raw_df[raw_df["user_review"] == "tbd"].index)
raw_df["user_review"] = pd.to_numeric(raw_df["user_review"])
print(raw_df.dtypes)

#make three dfs that contain only top 100 meta_score games from nintendo, sony and microsoft platforms

print(raw_df["platform"].value_counts())
nintendo = raw_df[raw_df["platform"].str.contains("Switch") + raw_df["platform"].str.contains("Nintendo") + raw_df["platform"].str.contains("Gamecube")
            + raw_df["platform"].str.contains("Wii") + raw_df["platform"].str.contains("DS") + raw_df["platform"].str.contains("3DS")
            + raw_df["platform"].str.contains("Game Boy Advance")]
nintendo = nintendo.reset_index()
nintendo.loc[:,'Company'] = "Nintendo"
nintendo = nintendo.iloc[0:100]
print(nintendo.head())
print(nintendo.shape)

sony = raw_df[raw_df["platform"].str.contains("PlayStation") + raw_df["platform"].str.contains("PSP")]
sony = sony.reset_index()
sony.loc[:,"Company"] = "Sony"
sony = sony.iloc[0:100]
print(sony.head())
print(sony.shape)
microsoft = (raw_df[raw_df["platform"].str.contains("Xbox")]).reset_index()
microsoft.loc[:,"Company"] = "Microsoft"
microsoft = microsoft.iloc[0:100]
print(microsoft.head())
print(microsoft.shape)

#contacanate three new dfs into one df and shaping new df

dtfs =[nintendo, sony, microsoft]
df = df = pd.concat(dtfs)
print(df["Company"].value_counts())
print(df.head())
del df["index"]

#changing release_date column to datetime and adding a column release_year

df["release_date"] = pd.to_datetime(df["release_date"])
df["release_year"] = df["release_date"].dt.year
print(df.head())

#adding a column great_game based on conditions

df["great_game"] = np.where(
    (df.meta_score >= 90) & (df.user_review >= 9.0),
    "yes",
    "no")
print(df.head())

#creating a df great_game that only has great games in it

great_game = df[df["great_game"].str.contains("yes")]
print(great_game.head())
print(great_game.isnull().sum())








