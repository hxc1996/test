import tensorflow as tf
import  numpy as np
# print(tf.__version__)
a=tf.constant([[1,2],[3,4]])#张量创建，参数value，dtype，shape
b=tf.constant([[1,2],[3,4]])
print(a)

#运用numpy创建张量
tf.constant(np.array(1))

#改变张量的数据类型
tf.cast(a,dtype=tf.float32)

#判断是否为张量
tf.is_tensor(a)
isinstance(a,tf.Tensor)

tf.zeros(shape=[2,2],dtype=tf.int32)
tf.ones(shape=[3,3],dtype=tf.int32)
tf.fill(dims=[4,4],value=9)

#正态分布
tf.random.normal(shape=[3,3,3],mean=0,stddev=2,dtype=tf.int32)
tf.random.truncated_normal(shape=[3,3,3],mean=0,stddev=2,dtype=tf.int32)
#truncated_normal阶段标准式2倍的标准差

#设置随机种子
tf.random.set_seed()

#创建均匀分布张量
tf.random.uniform(shape=[2,2],minval=1,maxval=5,dtype=tf.float32)

#随机打乱
tf.random.shuffle(a)

#创建序列
tf.range(start=2,lomit=10,delta=1,dtype=tf.float32)

#增加维度
tf.expand_dims(input=a,axis=0)
#删除维度
tf.squeeze(input=a,axis=0)
#交换维度
tf.transpose(input=a,perm=[1,0])
#拼接
tf.concat(a,b,axis=1)
#分割
tf.split(a,num_or_size_split=[1,2,1],axis=0)
#堆叠
tf.stack(a,b,axis=0)
#分解
tf.unstack(a,axis=1)

#数据提取
tf.gather(a,indices=[0,2],axis=0)
tf.gather_nd(a,[[0,0],[0,1]])

#运算
tf.add(a,b)
tf.subtract(a,b)
tf.multiply(a,b)
tf.divide(a,b)
tf.math.mod(a,b)
tf.pow(a,b)#a的b次冥
tf.square(a)
tf.sqrt(a)
tf.exp(a)
tf.math.log(a)

#向量乘法
tf.matmul(a,b)
a@b

