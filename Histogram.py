import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("world_happiness_dataset.csv")

# Clean data
data = data.dropna(subset=['Happiness Score', 'Region'])

# figure size
plt.figure(figsize=(12,7))

# Histogram 
sns.histplot(
    data=data, 
    x='Happiness Score', 
    hue='Region',               # color by Region
    multiple='stack',              # stacked bars
    bins=20,              
    kde=True,     
    palette='Set2',        
    edgecolor='black',
    alpha=0.8
)

# Add mean & median lines
plt.axvline(data['Happiness Score'].mean(), color='red', linestyle='--', linewidth=2, label='Mean')
plt.axvline(data['Happiness Score'].median(), color='green', linestyle='--', linewidth=2, label='Median')

# Labels
plt.xlabel('Happiness Score', fontsize=14)
plt.ylabel('Number of Countries', fontsize=14)
plt.title('Distribution of Happiness Score Across Countries', fontsize=16)
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

# Save the plot as png
plt.tight_layout()
plt.savefig("Happiness_Score_Histogram.png", dpi=300, bbox_inches='tight')
plt.show()
