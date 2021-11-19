rint(y["platform"].values)
plt.xticks(rotation=90)
sns.countplot(x="platform", data=y)
plt.tick_params(direction='out', length=6, width=2, labelsize=7, colors='r',
               grid_color='r', grid_alpha=0.5)
plt.subplots_adjust(bottom=0.25)
nintendo = y[y["platform"].str.contains("Switch") + y["platform"].str.contains("Nintendo") + y["platform"].str.contains("Gamecube")
            + y["platform"].str.contains("Wii") + y["platform"].str.contains("DS") + y["platform"].str.contains("3DS")]
sns.countplot(x="platform", data=y)
x.set_index("platform", inplace=True)
sony = y[y"platform"].str.contains("Play") + y[y"platform"].str.contains("PSP")
mcsoft = y[y["platform"].str.contains]
def set_value(row_number, assigned_value):
    return assigned_value[row_number]
dict = {"Switch" : "Nintendo", "Nintendo 64" : "Nintendo", "GameCube" : "Nintendo", "Wii" : "Nintendo", "Wii U" : "Nintendo",
        "DS" : "Nintendo", "3DS" : "Nintendo", "PlayStation 1" : "Sony", "PlayStatio 2" : "Sony", "PlayStation 3" : "Sony",
        "PlayStation 4" : "Sony", "PlayStation 5" : "Sony", "PlayStation Vita" : "Sony", "PSP" : "Sony", "DreamCast" : "Other",
        "Stadia" : "Other", "PC" : "PC", "Xbox 360" : "Microsoft", "Xbox One" : "Microsoft", "Xbox" : "Microsoft",
        "Xbox Series X" : "Microsoft"}
y.drop_column
y['Company'] = df['platform'].apply(set_value, args =(dict,))
