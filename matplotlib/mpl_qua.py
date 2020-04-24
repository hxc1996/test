import matplotlib.pyplot as plt
qua=[1,4,9,16,25]
input_values=[1,2,3,4,5]
plt.plot(input_values,qua,linewidth=5) #线条粗细

plt.title('qua number',fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('qua of value',fontsize=14)
plt.tick_params(axis='both',labelsize=14) #刻度字号
plt.show()