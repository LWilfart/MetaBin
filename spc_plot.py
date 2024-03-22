# Importation des bibliothèques
import pandas as pd
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Chemin vers le fichier CSV
csv_file = "/home/dydinux/TFE/10_Graph_GC_Cov_Binning/03/table/nt_03.csv"

# Lire le CSV
data = pd.read_csv(csv_file)

# Codes spécifiques que vous souhaitez inclure
specific_codes = ["CP000252.1", "CU466930.1", "AP019781.1", "HE964772.2", "OV788639.1", "CP070762.1", "CP046401.1", "CP002868.1", "CP070707.1", "LT549891.1"]

# Filtrer les données pour inclure uniquement les codes spécifiques
filtered_data = data[data['Code'].isin(specific_codes)]

# Liste de couleurs personnalisée avec 10 couleurs distinctes
custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Créer un dictionnaire de couleurs personnalisées pour les codes spécifiques
color_mapping = {code: color for code, color in zip(specific_codes, custom_colors)}

# Créer le scatterplot avec couleur en fonction de la colonne "Code"
scatter = plt.scatter(filtered_data['%GC'], filtered_data['Coverage'], c=filtered_data['Code'].map(color_mapping))
plt.xlabel('%GC')
plt.ylabel('Coverage')
plt.title('Scatterplot Coverage vs %GC')

# Créer une légende des codes de couleur
legend_patches = [mpatches.Patch(color=color_mapping[code], label=code) for code in specific_codes]
plt.legend(handles=legend_patches, title='Code', loc='center left', bbox_to_anchor=(1.02, 0.5))

# Afficher le scatterplot
plt.show()


