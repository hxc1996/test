import numpy as np
import matplotlib.pyplot as plt

x=2*np.random.random(size=100)
y=x*3.+4.+np.random.normal(size=100)

plt.scatter(x,y)
plt.show()

