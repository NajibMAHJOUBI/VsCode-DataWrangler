# Suppresion de la colonne Location
df.drop(columns=["Location"], inplace=True)

# Filtre des données de la ville de Montreal et de type 'Private room'
df = df[(df["City"] == 'Montreal') & (df["Accommodation type"] == "Private room")]