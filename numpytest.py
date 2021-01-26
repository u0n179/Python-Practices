import numpy as np
from numpy.core.overrides import array_function_dispatch
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

# matr1=np.mat("1 2 3;4 5 6;7 8 9")
# matr1b=np.matrix([[11,2,3],[4,51,6],[7,8,91]])
# print('mat Test\n',matr1)
# print('Matrix Test\n',matr1b)

# print('inverse test\n',matr1b.I)

# print('tansition test\n',matr1b.T)

# arr6=np.arange(100).reshape(10,10)
# arr7=np.arange(0,1.0,0.1).reshape(2,5)
# np.save("D:\\Codes\\Python\\test",arr6)
# np.savez("D:\\Codes\\Python\\test2",arr6,arr7)
# print('\n保存的数组为：\n',arr6,'\n第二个数组\n',arr7)

# load_arr=np.load("D:\\Codes\\Python\\test2.npz")
# print('\nload_test\n',load_arr['arr_0'])#arr_1代表npz第二个数组

# np.savetxt("D:\\Codes\\Python\\testtxt.txt",arr6,fmt="%d",delimiter=',')#路径、数组名、格式、分隔符
# load_txt=np.loadtxt("D:\\Codes\\Python\\testtxt",delimiter=',')#路径、分隔符

# arr8=np.random.randint(1,10,size=(3,3))
# print('original array=\n',arr8)

# arr8.sort(axis=1)
# print('\naxis=1\n',arr8)
# arr8.sort(axis=0)
# print('\naxis=0\n',arr8)

# arrA=np.array([3,34,5,1])
# arrB=np.array([4,3,13,5])
# arrC=np.array([3,4,1,39])
# sortD=np.lexsort((arrA,arrB,arrC))
# print('按照sortD的顺序排序',list(zip(arrA[sortD],arrB[sortD],arrC[sortD])))#类似贪心算法，依照c b a的顺序进行排序

# names=np.array(['小明','小黄','小花','小明','小花','小兰','小白'])
# print('创建的数组为：',names)
# print('\nunique去重\n',np.unique(names))

# arr9=np.arange(6)
# print('\noriginal array\n',arr9)
# print('\ntile x3\n',np.tile(arr9,3))

arr10=np.random.random(6)
arr10b=arr10.reshape(2,3)
print('original array',arr10)
print('\nvar方差\n',np.var(arr10))
print('\nmean均值\n',np.mean(arr10))#arr.mean(axis=1)也可以求列均值
print('\nsum和\n',np.sum(arr10))
print('\n数组的纵轴和\n',arr10b.sum(axis=0)) #按列求和
print('\ncumsum元素累计和\n',np.cumsum(arr10))#第一个值和原来相同 后面每个值都是从第一个值加到后面的和
print('\nargmin最小值索引\n',np.argmin(arr10))