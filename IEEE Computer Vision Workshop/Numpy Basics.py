import numpy as np

# a=np.array([1,2,3,4])
# print(a,type(a))
#
# b = [1,2,3,4]
# b = np.array(b)
#
# c = np.array((2,3), dtype=np.uint8) # Can pass a tuple aswell and datatype is fixed to 8 bit integer
# print(c)
#
# d = np.full((3,4),6,dtype = np.uint8)
# print(d)
#
# e = np.zeros((3,4),dtype = np.uint8)
# print(e)
# print(e.shape)
# rows, cols = e.shape                    # Assigning the variables
# print(rows, cols)
# print(f"({rows}, {cols})")              # Formatted print statement
# print(e.shape[0], e.shape[1])
#
# f = np.full((4,5,3),8,dtype=np.uint8)
# print(f.shape,f)


a = np.full((5,4),1,dtype=np.uint8)

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        print(a[i][j], end=' ')
    print()

