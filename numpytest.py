import numpy as np
from numpy.core.shape_base import vstack
#arr1=np.array([1,2,3,4])
#print('array is ',arr1,' shape is ',arr1.shape)
#print('使用 arange 函数创建的数组为：\n',np.arange(0,1,0.1))
#df=np.dtype([("name",np.str_,40),("numitems",np.int64),("price",np.float64)])
#print('数据类型为：',df)
# arr2=np.arange(10)
# print(arr2)
# arr3 = np.array([
# [1, 2, 3, 4, 5],
# [4, 5, 6, 7, 8], 
# [7, 8, 9, 10, 11]
# ])
# print('创建的二维数组为：\n',arr3)
# print('索引测试\n',arr3[1,3:5])
# print('多行索引测试\n',arr3[1:,2:])
# print('多列索引测试\n',arr3[:,2:])

# arr4=np.random.randn(3,3)
# arr4=np.arange(9)
# print('随机分布的数组\n',arr4)

# arr4=arr4.reshape(1,9)
# print('ReShape测试\n',arr4)

# arr5=arr4*5
# print('横向组合测试\n',np.hstack((arr4,arr5)))

# print('横向组合为：\n',np.hstack((arr4,arr5))) 

# print('纵向组合测试\n',np.vstack((arr4,arr5)))

matr1=np.mat("1 2 3;4 5 6;7 8 9")
matr1b=np.matrix([[11,2,3],[4,51,6],[7,8,91]])
print('mat Test\n',matr1)
print('Matrix Test\n',matr1b)