import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Path to csv
csv_file = "/home/dydinux/TFE/10_Graph_GC_Cov_Binning/02/6M200blastn-02sw/nouveau_table.csv"

# read CSV
data = pd.read_csv(csv_file)

# Get the unique values from the 'Code' column
unique_codes = data['Code'].unique()

# List of colors
custom_colors = ['#6495ed', '#dc143c', '#00ffff', '#00ff00', '#0000ff', '#8a2be2', '#a52a2a', '#deb887','#5f9ea0', '#7fff00', '#d2691e', '#ff69b4', '#00008b', '#008b8b', '#a9a9a9', '#006400','#bdb76b', '#8b008b', '#556b2f', '#ff8c69', '#9932cc', '#8b4513', '#2e8b57', '#ffebcd','#4169e1', '#da70d6', '#d2b48c', '#008080', '#d8bfd8', '#ff6347', '#40e0d0', '#ee82ee','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf', '#b0c4de', '#f08080', '#90ee90', '#ff00ff', '#808080', '#8b0000','#ff8c00', '#ffd700', '#008000', '#000080', '#4b0082', '#800080', '#808000', '#000000','#6495ed', '#dc143c', '#00ffff', '#00ff00', '#0000ff', '#8a2be2', '#a52a2a', '#deb887','#5f9ea0', '#7fff00', '#d2691e', '#ff69b4', '#00008b', '#008b8b', '#a9a9a9', '#006400','#bdb76b', '#8b008b', '#556b2f', '#ff8c69', '#9932cc', '#8b4513', '#2e8b57', '#ffebcd','#4169e1', '#da70d6', '#d2b48c', '#008080', '#d8bfd8', '#ff6347', '#40e0d0', '#ee82ee','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf', '#b0c4de', '#f08080', '#90ee90', '#ff00ff', '#808080', '#8b0000','#ff8c00', '#ffd700', '#008000', '#000080', '#4b0082', '#800080', '#808000', '#000000','#6495ed', '#dc143c', '#00ffff', '#00ff00', '#0000ff', '#8a2be2', '#a52a2a', '#deb887','#5f9ea0', '#7fff00', '#d2691e', '#ff69b4', '#00008b', '#008b8b', '#a9a9a9', '#006400', '#bdb76b', '#8b008b', '#556b2f', '#ff8c69', '#9932cc', '#8b4513', '#2e8b57', '#ffebcd','#4169e1', '#da70d6', '#d2b48c', '#008080', '#d8bfd8', '#ff6347', '#40e0d0', '#ee82ee','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf', '#b0c4de', '#f08080', '#90ee90', '#ff00ff', '#808080', '#8b0000','#ff8c00', '#ffd700', '#008000', '#000080', '#4b0082', '#800080', '#808000', '#000000']

# Check if the number of required colors is less than the list of custom colors.
if len(unique_codes) <= len(custom_colors):
    custom_palette = custom_colors[:len(unique_codes)]
else:
    raise ValueError("Verify if the number of colors needed is fewer than the number of custom colors available.")

# Create a dictionnary of colors
color_mapping = {code: color for code, color in zip(unique_codes, custom_palette)}

# Create label for colors
legend_patches = [mpatches.Patch(color=color_mapping[code], label=code) for code in unique_codes]

# Create scatter plot with color regarding the Code column
scatter = plt.scatter(data['%GC'], data['Coverage'], c=data['Code'].map(color_mapping))
plt.xlabel('%GC')
plt.ylabel('Coverage')
plt.title('Scatterplot Coverage vs %GC')

# Save the color code/organism code as an image
legend_fig = plt.figure(figsize=(2, 8)) 
plt.legend(handles=legend_patches, title='Code', loc='center')
plt.axis('off')
legend_fig.savefig('legend.png', bbox_inches='tight')
plt.close(legend_fig)  # do not show it

# show scatterplot
plt.show()


