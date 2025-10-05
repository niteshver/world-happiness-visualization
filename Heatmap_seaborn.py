import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
data = pd.read_csv("world_happiness_dataset.csv")
data = data.dropna()

# Only Numeric Data
numeric_data = data.select_dtypes(include='number')
corr = numeric_data.corr()

#mask 
mask = np.abs(corr) < 0.5

# Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(corr, annot=True, cmap="RdBu_r", fmt=".2f", linewidths=0.5, mask=mask)
plt.title("Correlation Heatmap of World Happiness Dataset", fontsize=16)

# Save chart
plt.savefig("Heatmap_seaborn.png", bbox_inches="tight", dpi=300)
plt.show()
