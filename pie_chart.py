import pandas as pd
import matplotlib.pyplot as plt
#load dataset
data = pd.read_csv("world_happiness_dataset.csv")
data = data.dropna()

#Pie Chart
country_counts = data['Region'].value_counts().head(15)
label = country_counts.index
sizes = country_counts.values
plt.pie(sizes,labels = label,autopct= '%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')

# Title
plt.title("Distribution of Countries by region",pad=20)
# Save chart as PNG File
plt.savefig("pie_chart.png",bbox_inches='tight',dpi=300)
plt.show()
