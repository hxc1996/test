count=0
def hanoi(n,scr,dst,mid):
    global count
    if n==1 :
        print("{}:{}->{}".format(1,scr,dst))
        count+=1
    else:
        hanoi(n-1,scr,dst,mid)
        print("{}:{}->{}".format(n,scr,dst))
        count+=1
        hanoi(n-1,mid,dst,scr)


hanoi(4,'a','b','c')
print(count)
