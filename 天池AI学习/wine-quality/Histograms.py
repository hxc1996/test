import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

color = sns.color_palette()
pd.set_option('precision',3)

df = pd.read_csv('D:\DataSet\winequality-red.csv',sep=';')

plt.style.use('ggplot')
colnm = df.columns.tolist()
fig = plt.figure(figsize=(10,8))
for i in range(12):
    plt.subplot(4,3,i+1)
    df[colnm[i]].hist(bins=100,color=color[0])
    plt.xlabel(colnm[i],fontsize=12)
    plt.ylabel('Frequency')

plt.tight_layout()
print('\nFigure 2: Univariate Histograms')
plt.show()

