#Library import
import pandas as pd
import matplotlib.pyplot as plt

# Path to CSV
csv_file = "path/to/your/file.csv"

# Read CSV
data = pd.read_csv(csv_file)

# Scatterplot creation
plt.scatter(data['%GC'],data['Coverage'])
plt.xlabel('%GC')
plt.ylabel('Coverage')
plt.title('Scatterplot Coverage vs %GC')

# Plot
plt.show()
