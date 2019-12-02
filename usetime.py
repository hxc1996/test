import time
print(time.time())
print(time.ctime())
print(time.gmtime())
t=time.gmtime()
d=time.strftime("%Y-%m-%d",t)
print(d)