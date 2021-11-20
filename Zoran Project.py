#import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.mode.chained_assignment = None

#import dataset

y = pd.read_csv("all_games.csv")

#checking for shape and missing data

print(y.head())
print(y.shape)
print(y.isnull().sum())

#delete summary column

del y["summary"]

#checking for data types

print(y.dtypes)

#user review should be float

print(y["user_review"].value_counts())

#drop tbd so we can change column type from object to float (first tbd game in place 679)

print(y[y["user_review"] == "tbd"])
y = y.drop(y[y["user_review"] == "tbd"].index)
y["user_review"] = pd.to_numeric(y["user_review"])
print(y.dtypes)

#make three dfs that contain only top 100 meta_score games from nintendo, sony and microsoft platforms

print(y["platform"].value_counts())
nintendo = y[y["platform"].str.contains("Switch") + y["platform"].str.contains("Nintendo") + y["platform"].str.contains("Gamecube")
            + y["platform"].str.contains("Wii") + y["platform"].str.contains("DS") + y["platform"].str.contains("3DS")
            + y["platform"].str.contains("Game Boy Advance")]
nintendo = nintendo.reset_index()
nintendo.loc[:,'Company'] = "Nintendo"
nintendo = nintendo.iloc[0:100]
print(nintendo.head())
print(nintendo.shape)

sony = y[y["platform"].str.contains("PlayStation") + y["platform"].str.contains("PSP")]
sony = sony.reset_index()
sony.loc[:,"Company"] = "Sony"
sony = sony.iloc[0:100]
print(sony.head())
print(sony.shape)
microsoft = (y[y["platform"].str.contains("Xbox")]).reset_index()
microsoft.loc[:,"Company"] = "Microsoft"
microsoft = microsoft.iloc[0:100]
print(microsoft.head())
print(microsoft.shape)

#contacanate three new dfs into one df and shaping new df

dtfs =[nintendo, sony, microsoft]
df = df = pd.concat(dtfs)
df = df.reset_index()
print(df["Company"].value_counts())
print(df.head())
del df["index"]
del df["level_0"]


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

#ploting point plot of average meta_score per company

g2 = sns.catplot(x="Company", y="meta_score", data=df, kind="point", ci=None)
plt.show()

#ploting line plot of average meata_score per year per company
g1 = sns.lineplot(x="release_year", y="meta_score", data=df, hue="Company", ci=None)
g1.set(xticks=df.release_year)
plt.xticks(rotation=90)
plt.show()

#plot corelation heatmap between meta_score and user_review

print(df["meta_score"].corr(df["user_review"]))
sns.heatmap(df.corr(), annot = True, fmt='.2g',cmap= 'coolwarm')
plt.show()

#plot point plot of mean user review per company

g3 = sns.catplot(x="Company", y="user_review", data=df, kind="point", ci=None)
plt.show()

##ploting line plot of mean meata_score per year per company

g4 = sns.lineplot(x="release_year", y="user_review", data=df, hue="Company", ci=None)
g4.set(xticks=df.release_year)
plt.xticks(rotation=90)
plt.show()

#plot countplot of amount of great games per company

sns.countplot(data=great_game, x="great_game", hue="Company")
plt.show()

#plot mean meta score and user review per platform

sns.catplot(data=df,x="platform", y="meta_score", kind="point", hue="Company", ci=None)
plt.xticks(rotation=90)
sns.catplot(data=df,x="platform", y="user_review", kind="point", hue="Company", ci=None)
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.30)
plt.show()






