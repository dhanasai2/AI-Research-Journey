import numpy as np
#Matrix multiplicatiion
"""
matrix1=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(matrix1@matrix2)
print(np.matmul(matrix1,matrix2))
print(np.dot(matrix1,matrix2))
"""
#Random function
"""
np.random.seed(42)
x1=np.random.randint(5,size=8)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))
print(x1)
print(x2)
print(x3)
print(x1.dtype)
print(x2.nbytes)
print(x3.itemsize)
print(x3[::2,:3])
x6=np.random.rand(3,3)
x7=np.random.randn(3,3)
print(x6)
print(x7)
#Boolean Indexing
"""
x4=np.array([[1,2,3,5,4],[1,3,4,5,6],[5,3,7,8,9]])
x5=np.array([1,2,3,4,5])
print(x4[x4>5])
print(x4[x4%2==0])
print(x4[x4&1==1])
print(x4.sum(axis=0))
print(x4.sum(axis=1))
print(x4+x5)



