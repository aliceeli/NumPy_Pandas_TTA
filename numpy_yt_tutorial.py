import numpy as np
a = np.array([1, 2, 3, 4, 5], dtype="int32")
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

#get dimension
print("dimension ", a.ndim)

#get shape
print("shape ", b.shape)

#get type
print("type ", a.dtype)

#get size
print("size ", a.itemsize)

#get total size
print("total size", a.size*a.itemsize, a.nbytes)

