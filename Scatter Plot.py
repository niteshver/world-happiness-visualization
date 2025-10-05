import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # USE ONLY FOR COLOR BY REGION

# Load Dataset
data = pd.read_csv("world_happiness_dataset.csv")
data = data.dropna(subset=["Economy (GDP per Capita)", "Happiness Score", "Region"])

# scatter plot
plt.figure(figsize=(12,7))
sns.scatterplot(
    x="Economy (GDP per Capita)",
    y="Happiness Score",
    hue="Region",          # color by region
    data=data,
    s=100,                
    alpha=0.7,             # transparency for overlapping 
    edgecolor="black"
)

# Labels
plt.xlabel("Economy (GDP per Capita)")
plt.ylabel("Happiness Score")
plt.title("Economy vs Happiness Score by Region")
plt.legend(title="Region", bbox_to_anchor=(1.05,1), loc='upper left')

# Save the chart
plt.tight_layout()
plt.savefig("Scatter_plot.png")
plt.show()
