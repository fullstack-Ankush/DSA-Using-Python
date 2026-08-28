from numpy import * 

# creating an array
val = array([1,4,2,2,1])

# solution 1
val.sort()

# solution 3
sum = 0
for i in val:
    sum += i 
    avg = sum//len(val)


# solution 4
n = int(input("Enter a number "))
l1 = []
for i in range(2,n+1):
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        l1.append(i)

# print(avg)
print(l1)
# print(val)