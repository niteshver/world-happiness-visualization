'''BAR CHART'''

import pandas as pd
import matplotlib.pyplot as plt

# Dataset load
data = pd.read_csv("world_happiness_dataset.csv")

# Remove missing values
data = data.dropna()

#Bar chart
plt.figure(figsize=(10,6))
plt.bar(data['Country'][:10], data['Happiness Score'][:10], color="skyblue")

# Labels
plt.xlabel("Country")
plt.ylabel("Happiness Score")
plt.title("Happiness Score of Top 10 Countries")
plt.xticks(rotation=45)

# Save the chart as PNG file
plt.savefig("bar_chart.png", bbox_inches='tight', dpi=300)
plt.show()
