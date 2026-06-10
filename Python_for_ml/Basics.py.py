import numpy as np
x1=np.array([[1,2,3],[4,5,6],[7,8,9]])
x2=np.array([1,2,3,4,5,6,7,8,9,10])
#basic of numpy arrays
""" 
print(x1.dtype)
print(x1)
x1[2,2]=92
print(x1[2,2])
print(x2[0:10:2])
print(x2[1:10:2])
print(x2[:4])
print(x2[::3]) 
"""
#array attribbutes
"""
print(x1.ndim)
print(x1.shape)
print(x1.size)
"""
#creating a basic array
"""
print(np.zeros((3,3)))
print(np.ones((4,4)))
print(np.arange(0,10,2))
"""
#Adding, removing, and sorting elements
"""
x3=np.array([10,5,8,3,6,4,2,1,9,7,0])
print(np.sort(x3))
x4=np.array([[1,2,3,],[4,5,6]])
x5=np.array([[9,8,7],[6,5,4]])
print(np.concatenate((x4,x5)))
"""
#Shape and resize
#ndarray.ndim will tell you the number of axes, or dimensions, of the array.
#ndarray.size will tell you the total number of elements of the array. This is the product of the elements of the array’s shape.
#ndarray.shape will display a tuple of integers that indicate the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3)

x6=np.array([[[1,2,3],[4,5,6],[7,8,9]],
             [[9,8,7],[6,5,4],[3,2,1]],
             [[1,3,2],[4,6,5],[7,9,8]]]
            )
"""
print(x6)
print(x6.ndim)
print(x6.size)
print(x6.shape)
"""
#Can you reshape an array
# print(x6.reshape(3,9))
#Converting 1D array to 2D array Using newaxis and expand_dims
"""
x7=np.array([1,2,3,4,5,6])
print(x7.shape)
x8=x7[np.newaxis,:]
print(x8.shape)
x9=np.expand_dims(x8,axis=1)
print(x9)
"""
#Indexing and slicing
"""
x10=np.array([1,2,3,4,5,6,7,8,9])
x11=np.array([[[1,2,3,4,5],[5,4,3,2,1]],[[6,7,8,9,0],[0,9,8,7,6]],[[1,3,5,7,9],[9,7,5,3,1]]])
print(x10.shape)
print(x10[5])
print(x10[1:9:2])
print(x10[::3])
print(x10[:5])
print(x10[0::])
print(x10[0::4])
print(x10[:10:2])
print(x11[x11>5])
"""
#How to create an array from existing data
"""
x12=np.array([1,2,3,4,5,6,7,8,9])
x12copy=x12[4:8]
print(x12copy)
#vstack and hstack
x13a=np.array([[1,2,3],[4,5,6],[7,8,9]])
x13b=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(np.vstack((x13a,x13b)))
print(np.hstack((x13a,x13b)))
x14=np.arange(1,31).reshape(3,10)
print(x14)
x15=np.hsplit(x14,2)
print(x15)
"""
#Basic array operations
"""
x16=np.array([[1,3,5],[2,4,6],[8,6,4]])
x17=np.array([[2,4,6],[1,3,5],[5,8,3]])
print(x16+x17)
print(x16-x17)
print(x16*x17)
print(x16/x17)
print(x16.sum())
"""
#Broadcasting
"""
b1=np.array([[1],
             [2],
             [3]])
#print(b1.shape)
b2=np.array([1,2,3,4])
#print(b2)
print(b1+b2)
print(b1*b2)
"""
#More useful array operations
"""
b3=np.array([[[5,3,1],[2,3,4]],[[9,6,3],[5,2,3]],[[1,2,3],[5,2,3]]])
print(b3)
print(b3.sum())
print(b3.max())
print(b3.min())
"""
#Creating matrices
"""
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix1=np.array([[3,2,1],[6,5,4],[9,8,7]])
#print(matrix)
print(matrix+matrix1)
print(matrix[0:3])
print(matrix.sum())
print(matrix.max())
print(matrix.min())
print(matrix.max(axis=0))
print(matrix1.max(axis=1))
# main point axis=0 -> operate vertically (column-wise) and axis=1 → operate horizontally (row-wise)
"""
#Transposing and reshaping a matrix
matrix2=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix3=np.array([[3,2,1],[6,5,4],[9,8,7]])
print(matrix2.reshape(1,9))
print(matrix3.transpose())
print(matrix2.T)