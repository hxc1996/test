import matplotlib.pyplot as plt

x_value=list(range(1,1001))
y_value=[x**2 for x in x_value]
plt.scatter(x_value,y_value,s=40,edgecolors='none',c=y_value,cmap=plt.cm.Blues)

plt.title('qua number',fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('qua of value',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14) #刻度字号
plt.axis([0,1100,0,1100000])
plt.show()
# plt.savefig('D:\\11.png',bbox_inches='tight')