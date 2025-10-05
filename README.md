# 🌍 World Happiness Data Visualization

## Project Overview
This project explores the **World Happiness Dataset** and visualizes the relationships between **Happiness Score** and various factors such as GDP, Social Support, Freedom, Life Expectancy, Generosity, and Perceptions of Corruption.  

The goal is to **understand patterns, correlations, and trends** that influence happiness across countries using **multiple data visualization techniques**.

---

## Dataset
- Source: [World Happiness Report Dataset](https://www.kaggle.com/datasets/unsdsn/world-happiness)
- Metrics include:
  - `Happiness Score`
  - `Economy (GDP per Capita)`
  - `Social Support`
  - `Healthy Life Expectancy`
  - `Freedom`
  - `Generosity`
  - `Perceptions of Corruption`
  - `Region`

---

## Visualizations

### 1️⃣ Histogram
- **Purpose:** Show distribution of Happiness Score across countries.
- **Features:**
  - KDE curve to smooth distribution
  - Mean and median lines
  - Region-wise stacked bars
- **Screenshot:**
![Histogram](images/histogram.png)

### 2️⃣ Pie Chart
- **Purpose:** Show distribution of countries by Region.
- **Features:**
  - Top 15 regions visualized
  - Percentage annotations
- **Screenshot:**
![Pie Chart](images/pie_chart.png)

### 3️⃣ Bar Chart
- **Purpose:** Compare Happiness Scores or other metrics across top countries.
- **Features:**
  - Sorted by Happiness Score or GDP
  - Color-coded by Region
- **Screenshot:**
![Bar Chart](images/bar_chart.png)

### 4️⃣ Heatmap
- **Purpose:** Show correlations between numeric features.
- **Features:**
  - Annotated correlation values
  - Diverging color palette for better visual contrast
- **Screenshot:**
![Heatmap](images/heatmap.png)

### 5️⃣ Scatter Plot
- **Purpose:** Explore relationships between numeric features (e.g., GDP vs Happiness Score)
- **Features:**
  - Color-coded by Region
  - Log scaling for skewed features (GDP)
  - Optional annotation for top/bottom countries
- **Screenshot:**
![Scatter Plot](images/scatter_plot.png)

---

## Key Insights
- GDP per Capita, Social Support, and Life Expectancy show strong positive correlation with Happiness Score.  
- Generosity has weaker correlation with Happiness.  
- Countries cluster by region: European countries generally have higher Happiness Scores, while some African countries cluster at lower scores.  
- Skewed features like GDP are better visualized on a log scale.

---

## Technologies Used
- **Python 3**
- **Libraries:** `pandas`, `matplotlib`, `seaborn`, `numpy`, `plotly` (optional for interactive plots)
- **IDE:** VS Code / Jupyter Notebook

---

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/yourusername/world-happiness-visualization.git
