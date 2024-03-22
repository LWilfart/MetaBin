# Importation des bibliothèques
import pandas as pd
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Chemin vers le fichier CSV
csv_file = "/home/dydinux/TFE/10_Graph_GC_Cov_Binning/03/table/nt_03.csv"

# Lire le CSV
data = pd.read_csv(csv_file)

# Obtenir les valeurs uniques de la colonne "Code"
unique_codes = data['Code'].unique()

# Liste de couleurs personnalisée pour un meilleur contraste sur fond blanc
custom_colors = ['#6495ed', '#dc143c', '#00ffff', '#00ff00', '#0000ff', '#8a2be2', '#a52a2a', '#deb887','#5f9ea0', '#7fff00', '#d2691e', '#ff69b4', '#00008b', '#008b8b', '#a9a9a9', '#006400','#bdb76b', '#8b008b', '#556b2f', '#ff8c69', '#9932cc', '#8b4513', '#2e8b57', '#ffebcd','#4169e1', '#da70d6', '#d2b48c', '#008080', '#d8bfd8', '#ff6347', '#40e0d0', '#ee82ee','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf', '#b0c4de', '#f08080', '#90ee90', '#ff00ff', '#808080', '#8b0000','#ff8c00', '#ffd700', '#008000', '#000080', '#4b0082', '#800080', '#808000', '#000000','#6495ed', '#dc143c', '#00ffff', '#00ff00', '#0000ff', '#8a2be2', '#a52a2a', '#deb887','#5f9ea0', '#7fff00', '#d2691e', '#ff69b4', '#00008b', '#008b8b', '#a9a9a9', '#006400','#bdb76b', '#8b008b', '#556b2f', '#ff8c69', '#9932cc', '#8b4513', '#2e8b57', '#ffebcd','#4169e1', '#da70d6', '#d2b48c', '#008080', '#d8bfd8', '#ff6347', '#40e0d0', '#ee82ee','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf', '#b0c4de', '#f08080', '#90ee90', '#ff00ff', '#808080', '#8b0000','#ff8c00', '#ffd700', '#008000', '#000080', '#4b0082', '#800080', '#808000', '#000000','#6495ed', '#dc143c', '#00ffff', '#00ff00', '#0000ff', '#8a2be2', '#a52a2a', '#deb887','#5f9ea0', '#7fff00', '#d2691e', '#ff69b4', '#00008b', '#008b8b', '#a9a9a9', '#006400', '#bdb76b', '#8b008b', '#556b2f', '#ff8c69', '#9932cc', '#8b4513', '#2e8b57', '#ffebcd','#4169e1', '#da70d6', '#d2b48c', '#008080', '#d8bfd8', '#ff6347', '#40e0d0', '#ee82ee','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf', '#b0c4de', '#f08080', '#90ee90', '#ff00ff', '#808080', '#8b0000','#ff8c00', '#ffd700', '#008000', '#000080', '#4b0082', '#800080', '#808000', '#000000']


# Vérifier si le nombre de couleurs nécessaires est inférieur à la liste des couleurs personnalisées
if len(unique_codes) <= len(custom_colors):
    custom_palette = custom_colors[:len(unique_codes)]
else:
    raise ValueError("Pas assez de couleurs dans la palette personnalisée pour les codes uniques.")

# Créer un dictionnaire de couleurs personnalisées
color_mapping = {code: color for code, color in zip(unique_codes, custom_palette)}

# Créer le scatterplot avec couleur en fonction de la colonne "Code"
scatter = plt.scatter(data['%GC'], data['Coverage'], c=data['Code'].map(color_mapping))
plt.xlabel('%GC')
plt.ylabel('Coverage')
plt.title('Scatterplot Coverage vs %GC')

# Créer une légende des codes de couleur
legend_patches = [mpatches.Patch(color=color_mapping[code], label=code) for code in unique_codes]
plt.legend(handles=legend_patches, title='Code', loc='center left', bbox_to_anchor=(1.02, 0.5))

# Afficher le scatterplot
plt.show()


