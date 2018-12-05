from collections import  deque
import  time

t = time.time()
d = deque([2,4,8,3,5,7])
d.append(8)
d.append(9)
print(len(d))
print(d[len(d)//2])