#Importation Librairie
import pandas as pd
import matplotlib.pyplot as plt

# Path vers CSV
csv_file = "/home/dydinux/TFE/10_Graph_GC_Cov_Binning/03/table/nt_03.csv"

# Lire le CSV
data = pd.read_csv(csv_file)

# Créer scatterplot
plt.scatter(data['%GC'],data['Coverage'])
plt.xlabel('%GC')
plt.ylabel('Coverage')
plt.title('Scatterplot Coverage vs %GC')

# scatterplot
plt.show()
