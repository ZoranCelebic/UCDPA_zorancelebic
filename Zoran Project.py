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

y["summary"].fillna("No Summary", inplace=True)

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

#changing user review by multiplying it with 10 to make it comparable to meta score

def times_10(x):
    return x * 10

df["user_review"] =(df["user_review"]).apply(times_10)


#creating a df great_game that only has great games in it

df["meta_user"] = (df["meta_score"] + df["user_review"]) / 2
conditions = [
    (df['meta_score'] >= 90) & (df['user_review'] >= 90),
    (df['meta_score'] < 90) & (df['user_review'] < 90),
    (df['meta_score'] > 90) & (df['user_review'] <= 90),
    (df['meta_score'] <= 90) & (df['user_review'] > 90)]
val = ["yes", "no", "no", "no"]

df["great_game"] = np.select(conditions, val)


great_game = df[df["great_game"].str.contains("yes")]

#ploting point plot of average meta_score per company

sns.set_style("darkgrid")
g1 = sns.catplot(x="Company", y="meta_score", data=df, kind="box", ci=None, palette=["r", "b", "g"])
g1.fig.suptitle("Meta score distribution per company", y=0.99, color="red",)
g1.set(xlabel="Company", ylabel = "Meta Score")
g1.set_xticklabels(color="darkblue")
g1.set_yticklabels(color="darkblue")
plt.savefig("average_meta_score_per_company.jpg")
plt.show()

#ploting line plot of average meta_score per year per company

sns.set_style("ticks")
g2 = sns.lineplot(x="release_year", y="meta_score", data=df, hue="Company", ci=None, palette=["r", "b", "g"], alpha=0.7, style="Company")
g2.set_title("Average meta score per company 1995.-2021.", y=1.05, color="red",)
g2.set(xlabel="Release year", ylabel="Average meta score")
g2.tick_params(axis="x", colors="darkblue")
g2.tick_params(axis="y", colors="darkblue")
g2.set(xticks=df.release_year)
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.15)
plt.savefig("average_meta_score_per_company_per_year.jpg")
plt.show()

#plot point plot of mean user review per company

sns.set_style("darkgrid")
g3 = sns.catplot(x="Company", y="user_review", data=df, kind="box", ci=None, palette=["r", "b", "g"], whis=[5, 95])
g3.fig.suptitle("User review distribution per company", color="red", y=0.98)
g3.set(xlabel="Company", ylabel="User review")
g3.set_xticklabels(color="darkblue")
g3.set_yticklabels(color="darkblue")
plt.savefig("average_user_review_per_company.jpg")
plt.show()

#ploting line plot of mean meata_score per year per company

sns.set_style("ticks")
g4 = sns.lineplot(x="release_year", y="user_review", data=df, hue="Company", ci=None, palette=["r", "b", "g"], alpha=0.7, style="Company")
g4.set_title("Average user score per company 1995.-2021.", y=1.05, color="red",)
g4.set(xlabel="Release year", ylabel="Average user review")
g4.tick_params(axis="x", colors="darkblue")
g4.tick_params(axis="y", colors="darkblue")
g4.set(xticks=df.release_year)
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.15)
plt.savefig("average_user_review_per_company_per_year.jpg")
plt.show()

#plot mean meta score and user review per platform

sns.set_style("darkgrid")
g5 = sns.catplot(data=df,x="platform", y="meta_score", kind="point", hue="Company", ci=None, palette=["r", "b", "g"])
g5.fig.suptitle("Meta score per platform", color="red", y=0.98)
g5.set(xlabel="Company", ylabel="Meta Score")
g5.set_xticklabels(color="darkblue")
g5.set_yticklabels(color="darkblue")
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.35)
plt.savefig("Meta score per platform.jpg")
plt.show()

g6 = sns.catplot(data=df,x="platform", y="user_review", kind="point", hue="Company", ci=None, palette=["r", "b", "g"])
g6.fig.suptitle("User score per platform", color="red", y=0.98)
g6.set(xlabel="Company", ylabel="User score")
g6.set_xticklabels(color="darkblue")
g6.set_yticklabels(color="darkblue")
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.35)
plt.savefig("User score per platform.jpg")
plt.show()

#plot median meta_user

from numpy import median
g7 = sns.catplot(x="Company", y="meta_user", data=df, kind="point", ci=None, estimator=median, palette=["r", "b", "g"])
g7.fig.suptitle("Median Meta_User/2 score per company", y=0.99, color="red",)
g7.set(xlabel="Company", ylabel = "Meta_user score")
g7.set_xticklabels(color="darkblue")#
g7.set_yticklabels(color="darkblue")
plt.savefig("average_meta_user_per_company.jpg")
plt.show()

#plot corelation heatmap

g8 = sns.heatmap(df.corr(), annot=True, fmt=".2g", cmap="coolwarm",
                 xticklabels=["Meta Score", "User review", "Release year", "Meta User"],
                 yticklabels=["Meta Score", "User review", "Release year", "Meta User"])
plt.savefig("Corelation heatmap")
plt.show()


g9 = sns.countplot(x="Company", data=great_game, palette=["r", "b", "g"])
g9.set_title("Number of Great games per company", color="red", y=1.05)
g9.set(xlabel="Company", ylabel="Number of games")
g9.tick_params(axis="x", colors="darkblue")
g9.tick_params(axis="y", colors="darkblue")
plt.savefig("Number of great games per platform.jpg")
plt.show()







