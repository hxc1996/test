import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

color = sns.color_palette()
pd.set_option('precision',3)

df = pd.read_csv('D:\DataSet\winequality-red.csv',sep=';')

plt.style.use('ggplot')
plt.figure(figsize=(6,3))

bins = 10**(np.linspace(-2, 2))
plt.hist(df['fixed acidity'], bins = bins, edgecolor = 'k', label = 'Fixed Acidity')
plt.hist(df['volatile acidity'], bins = bins, edgecolor = 'k', label = 'Volatile Acidity')
plt.hist(df['citric acid'], bins = bins, edgecolor = 'k', label = 'Citric Acid')
plt.hist(df['free sulfur dioxide'], bins = bins, edgecolor = 'k',  label = 'free sulfur dioxide')
plt.hist(df['sulphates'], bins = bins, edgecolor = 'k', alpha = 0.8,label = 'sulphates')
plt.hist(df['total sulfur dioxide'], bins = bins, edgecolor = 'k', alpha = 0.8, label = 'total sulfur dioxide')

plt.xscale('log')
plt.xlabel('Acid Concentration (g/dm^3)')
plt.ylabel('Frequency')
plt.title('Histogram of Acid Concentration')
plt.legend()
plt.tight_layout()

print('Figure 4')
plt.show()

