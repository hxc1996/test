import turtle
turtle.setup(650,350,200,200)  #窗体生成：长，宽，X，Y
turtle.penup() #调用画笔
turtle.fd(-250) #前进方向 bk反方向
turtle.pendown() #开始画图
turtle.pensize(25) #width
turtle.pencolor('purple')
turtle.seth(-40) #改变方向
for i in range(4):
    turtle.circle(40,80) #弧线：半径，弧度
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done() #保持程序运行完不退出
