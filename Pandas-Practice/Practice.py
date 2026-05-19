import pandas as pd
data = {
    "Player": ["Messi", "Ronaldo", "Saka", "Mbappe", "Neymar"],
    "Goals": [30, 28, 15, 32, 20],
    "Assists": [12, 8, 10, 9, 14]
}
df = pd.DataFrame(data)
Goals_column=df["Goals"]
rows_13=Goals_column.iloc[1:4]
print(df.loc[df["Player"]=="Mbappe"])
df["Contribution"]=df["Goals"]+df["Assists"]
print(df[df["Goals"]>20])