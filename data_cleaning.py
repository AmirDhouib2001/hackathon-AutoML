import pandas as pd
import os

DATA_FOLDER = "data"
OUTPUT_FILE = "final_data.csv"

caracteristiques_file = "caract-2023.csv"
lieux_file = "lieux-2023.csv"
vehicules_file = "vehicules-2023.csv"
usagers_file = "usagers-2023.csv"

print("Chargement des fichiers...")
caracteristiques = pd.read_csv(os.path.join(DATA_FOLDER, caracteristiques_file), sep=';', on_bad_lines='skip', engine='python')
lieux = pd.read_csv(os.path.join(DATA_FOLDER, lieux_file), sep=';', on_bad_lines='skip', engine='python')
vehicules = pd.read_csv(os.path.join(DATA_FOLDER, vehicules_file), sep=';', on_bad_lines='skip', engine='python')
usagers = pd.read_csv(os.path.join(DATA_FOLDER, usagers_file), sep=';', on_bad_lines='skip', engine='python')

print("Suppression des doublons...")
caracteristiques.drop_duplicates(inplace=True)
lieux.drop_duplicates(inplace=True)
vehicules.drop_duplicates(inplace=True)
usagers.drop_duplicates(inplace=True)

print(" Fusion des fichiers...")
df = pd.merge(usagers, vehicules, on=['Num_Acc', 'id_vehicule'], how='inner')
df = pd.merge(df, caracteristiques, on='Num_Acc', how='inner')
df = pd.merge(df, lieux, on='Num_Acc', how='inner')

print("Taille du dataset final :", df.shape)
print("Aperçu des premières lignes :\n", df.head())

print("Sauvegarde des données fusionnées...")
df.to_csv(OUTPUT_FILE, index=False)
print(f"Données fusionnées sauvegardées dans : {OUTPUT_FILE}")
