import  numpy as np
import  time
import sys
# ar = np.arange(1000)
# s = (range(1000))
# print(sys.getsizeof(s))
# print(ar.itemsize)

#time analysis
# SIZE = 100000
# n1 = np.arange(SIZE)
# n2 = np.arange(SIZE)
#
# start = time.time()
#
# n3 = n1+n2
# print('numpy time ', (time.time()-start)*1000)
#
# l1 = list(range(SIZE))
# l2 = list(range(SIZE))
#
# start = time.time()
# l3 = [ x+y  for x,y in zip(l1,l2)]
# print('list time ', (time.time()-start)*1000)
#
# print(n3[5], l3[5])


#  SOME MORE USEFUL OPERATIONS

n = np.array(([1,2,3],[4,5,6]))
print(np.ones(7,int))
print(n.ndim, n.size, n.shape, n.itemsize)
print(n.reshape(2,3)) # this product should be equal to size of an array
print(np.zeros(5,int), np.ones(10, float), np.linspace(1,10, 7)) # last one is splitting into 7 bits
print(n.max(), n.min(), n.sum())


# axis 0 is for columns, 1 for rows
print('Column sum -' , n.sum(axis=0), 'row sum ',n.sum(axis=1))

# slicing with numoy and usual method


m = np.array([[1,2,3],[2,3,4],[5,6,7],[8,9,0]])

print(m[:,2]) # every second element

print(m[1:3,2])   # only 1st n 2nd's 3rd element

print([xs[2] for xs in (ys for ys in m)])   # normal list comp way

print(m)
print(np.sqrt(m)) # doesnot alter the original array
print(m)


