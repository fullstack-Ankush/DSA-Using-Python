import numpy as np

#solution 1 

array1 = np.array([2,2,1,33,4])
result = sorted(array1,reverse=False)

print(result)

# solution 2

sample1 = ["abc",1,1.5,2,3,5,True]

for i in sample1:
    if type(i) != type(1):
        sample1.remove(i)

print(sample1)