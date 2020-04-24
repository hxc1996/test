import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

color = sns.color_palette()
pd.set_option('precision',3)

df = pd.read_csv('D:\DataSet\winequality-red.csv',sep=';')

plt.style.use('ggplot')
df['sweetness'] = pd.cut(df['residual sugar'], bins = [0, 4, 12, 45], labels=["dry", "medium dry", "semi-sweet"])
fig = plt.figure(figsize=(5,3))
df['sweetness'].value_counts().plot(kind = 'bar', color = color[0])
plt.xticks(rotation=0)
plt.xlabel('sweetness', fontsize = 12)
plt.ylabel('Frequency', fontsize = 12)
plt.tight_layout()
print("Figure 6: Sweetness")
plt.show()

