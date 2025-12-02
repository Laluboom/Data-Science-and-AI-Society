# Python Workshop – Data Visualization Guide
# ============================================================================
# Topics Covered:
# 1. Setup & Data Loading
# 2. Univariate Analysis (Histograms & Box Plots)
# 3. Categorical Analysis (Bar Charts)
# 4. Bivariate Analysis (Scatter Plots)
# 5. Multivariate Analysis (Pair Plots & Heatmaps)
# 6. Advanced Plots (Facet Grids & Violin Plots)
#
# Dataset: Iris Flowers (150 samples, 4 features, 3 species)
#
# Each section includes:
#   - Explanation of the plot type
#   - Executable Code
#   - "Try it Yourself" mini-tasks
# ============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ============================================================================
# 1. SETUP & DATA LOADING
# ============================================================================

# Before visualization, we must load our data.
# We are using the 'Iris' dataset, known as the "Hello World" of data science.
# It contains measurements for 150 iris flowers across 3 species.

print("--- [1] Loading Data ---")

# Load dataset from Seaborn's built-in library
iris = sns.load_dataset('iris')

# Inspect the data
print(f"Shape: {iris.shape}")
print(iris.head())
print(f"\nSpecies found: {iris['species'].unique()}")

# ----------------------------------------------------------------------------
# TRY IT YOURSELF:
# Use the .info() or .describe() method to see a statistical summary
# of the dataset below.
# ----------------------------------------------------------------------------

# iris.describe()


# ============================================================================
# 2. UNIVARIATE ANALYSIS (One Variable)
# ============================================================================

# Univariate analysis looks at one variable at a time.
# Common plots:
# 1. Histogram: Shows frequency distribution (shape of data).
# 2. Box Plot: Shows median, quartiles, and outliers.

print("\n--- [2] Generating Histograms & Box Plots ---")

# --- Example A: Histogram ---
plt.figure(figsize=(10, 5))
plt.hist(iris['sepal_length'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Histogram: Sepal Length Distribution')
plt.show()

# --- Example B: Box Plot ---
# Great for spotting outliers (dots beyond the whiskers)
plt.figure(figsize=(10, 5))
sns.boxplot(data=iris, orient='h', palette="Set2")
plt.title('Box Plot: All Numeric Features')
plt.show()

# ----------------------------------------------------------------------------
# TRY IT YOURSELF:
# Create a histogram for 'petal_length'. 
# Try changing the color to 'salmon' and bins to 15.
# ----------------------------------------------------------------------------

# plt.figure(figsize=(8, 4))
# plt.hist(iris['petal_length'], bins=15, color='salmon', edgecolor='black')
# plt.title('My Petal Length Histogram')
# plt.show()


# ============================================================================
# 3. CATEGORICAL ANALYSIS
# ============================================================================

# When dealing with text categories (like Species), we use Bar Charts or Count Plots.
# These show how many items belong to each category.

print("\n--- [3] Generating Categorical Plots ---")

# Using Seaborn's countplot (automatically counts rows per category)
plt.figure(figsize=(8, 5))
sns.countplot(data=iris, x='species', palette='pastel', edgecolor='black')

plt.title('Count Plot: Number of samples per Species')
plt.ylabel('Count')
plt.xlabel('Species')
plt.show()

# ----------------------------------------------------------------------------
# TRY IT YOURSELF:
# Create a Horizontal Bar Chart using y='species' instead of x='species'.
# ----------------------------------------------------------------------------

# sns.countplot(data=iris, y='species', palette='viridis')
# plt.show()


# ============================================================================
# 4. BIVARIATE ANALYSIS (Two Variables)
# ============================================================================

# Bivariate analysis finds relationships between two variables.
# The Scatter Plot is the most common tool here.
# Hue: We use the 'hue' argument to color points by a 3rd variable (Species).

print("\n--- [4] Generating Scatter Plots ---")

# Scatter Plot: Petal Length vs Petal Width
plt.figure(figsize=(10, 6))

sns.scatterplot(data=iris, 
                x='petal_length', 
                y='petal_width', 
                hue='species',      # Color by species
                style='species',    # Different shapes per species
                s=100)              # Size of dots

plt.title('Scatter Plot: Petal Dimensions by Species')
plt.show()

# ----------------------------------------------------------------------------
# TRY IT YOURSELF:
# Create a scatter plot comparing 'sepal_length' (x) vs 'sepal_width' (y).
# Set hue='species'.
# ----------------------------------------------------------------------------

# sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
# plt.show()


# ============================================================================
# 5. MULTIVARIATE ANALYSIS (Correlations & Pair Plots)
# ============================================================================

# When you have many variables, checking them one by one is slow.
# 1. Heatmap: Shows correlation strength (Red = Strong, Blue = Weak).
# 2. Pair Plot: Draws scatter plots for EVERY pair of variables.

print("\n--- [5] Generating Heatmaps & Pair Plots ---")

# --- Example A: Correlation Heatmap ---
# Select only numeric columns for correlation calculation
numeric_cols = iris.select_dtypes(include=[np.number])
corr_matrix = numeric_cols.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

# --- Example B: Pair Plot ---
# This is a powerful one-line command to summarize the whole dataset
sns.pairplot(iris, hue='species', height=2.5)
plt.suptitle('Pair Plot of Iris Data', y=1.02)
plt.show()

# ----------------------------------------------------------------------------
# TRY IT YOURSELF:
# Look at the Heatmap. Which two features have the highest positive correlation?
# (Look for the number closest to 1.0, usually dark red).
# ----------------------------------------------------------------------------

# Answer: Petal Length and Petal Width (0.96)


# ============================================================================
# 6. ADVANCED PLOTS (Violin & Facet Grids)
# ============================================================================

# 1. Violin Plot: Combines a box plot and a density plot (histogram).
#    It shows the "fatness" of the distribution.
# 2. Facet Grid: Creates multiple small charts side-by-side.

print("\n--- [6] Generating Advanced Plots ---")

# --- Example A: Violin Plot ---
plt.figure(figsize=(10, 6))
sns.violinplot(data=iris, x='species', y='petal_length', palette='muted')
plt.title('Violin Plot: Petal Length distribution per Species')
plt.show()

# --- Example B: Facet Grid ---
# Create a separate scatter plot for every species
g = sns.FacetGrid(iris, col='species', height=4)
g.map(plt.scatter, 'sepal_length', 'sepal_width', alpha=0.7)
g.add_legend()
plt.subplots_adjust(top=0.85)
g.fig.suptitle('Facet Grid: Sepal Dimensions split by Species')
plt.show()

# ----------------------------------------------------------------------------
# TRY IT YOURSELF:
# Create a Box Plot (sns.boxplot) comparing:
# x='species' and y='sepal_width'
# ----------------------------------------------------------------------------

# sns.boxplot(data=iris, x='species', y='sepal_width')
# plt.show()