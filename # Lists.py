# Lists
numbers = [1,2,3,5,8,13]
numbers[2] = 7
print(numbers)
#Exercise
N = [3,6,2,8,4,10,13]

#Suppose if
max = N[2]
for i in N:
    if i >  max:
        max =  i
print(max)

# 2D Lists

matrix  = [
    [1,2,3],
    [4,5,6],
    [-1,-2,3]
]
print(matrix[0][1])
# [1] gives the second element of the first element(list) of the matrix
for row in matrix:
    for column in row:
        print(column)


num = [5,2,1,7,4]
num.append(11)
print(num)
# 'append' command adds an element in the list
# 'instert(insert,element) replaces the element of that index
num.insert(0,30)
print(num)