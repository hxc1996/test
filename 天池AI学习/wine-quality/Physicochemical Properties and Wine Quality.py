import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

color = sns.color_palette()
pd.set_option('precision',3)

df = pd.read_csv('D:\DataSet\winequality-red.csv',sep=';')
df['total acid'] = df['fixed acidity'] + df['volatile acidity'] + df['citric acid']
plt.style.use('ggplot')
sns.set_style('ticks')
# 主题
# darkgrid 黑色网格（默认）
# whitegrid 白色网格
# dark 黑色背景
# white 白色背景
# ticks 应该是四周都有刻度线的白背景
sns.set_context("notebook", font_scale= 1.1)

colnm = df.columns.tolist()[:11] + ['total acid']
plt.figure(figsize = (10, 8))

for i in range(12):
    plt.subplot(4,3,i+1)
    sns.boxplot(x ='quality', y = colnm[i], data = df, color = color[1], width = 0.6)
    plt.ylabel(colnm[i],fontsize = 12)
plt.tight_layout()
print("\nFigure 7: Physicochemical Properties and Wine Quality by Boxplot")


sns.set_style("dark")

plt.figure(figsize = (10,8))
colnm = df.columns.tolist()[:11] + ['total acid', 'quality']
mcorr = df[colnm].corr()
mask = np.zeros_like(mcorr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
cmap = sns.diverging_palette(220, 10, as_cmap=True)
g = sns.heatmap(mcorr, mask=mask, cmap=cmap, square=True, annot=True, fmt='0.2f')
print("\nFigure 8: Pairwise Correlation Plot")
plt.show()