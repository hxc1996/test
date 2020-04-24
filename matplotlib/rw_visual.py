from matplotlib import pyplot as plt
from random_walk import RandomWalk

while True :
    rw=RandomWalk(50000)
    rw.fill_walk()

    #设置绘图窗口尺寸
    plt.figure(figsize=(8,6),dpi=128)
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,s=1,c=point_number,cmap=plt.cm.Blues,edgecolors='none')

    #突出起点与终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("make another walk?(y/n):")
    if keep_running == 'n':
        break