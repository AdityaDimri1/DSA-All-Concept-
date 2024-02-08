# Problem-1
# Write a Python program for Binary representation of a number, convert to integer.

# Example 
# Input : (1, 1, 1) 
# Output : 7 
# Explanation : 4 + 2 + 1 = 7.

# Code :

binaryTuple=(1,1,1)
print('Input tuple is :',binaryTuple)

convert = int("".join(str(element) for element in binaryTuple), 2) 
print('Decimal of the tuple : ',convert)


# Problem-2
# Write a Python program for Elements Frequency in Mixed Nested Tuple

# Example
# Input : (5, 6, (5, 6), 7, (8, 9), 9)
# Output : {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}

# Code :

inputTuple = (5, 6, (5, 6), 7, (8, 9), 9)
print("The original tuple : " + str(inputTuple))
 
eleList=[]
for ele in inputTuple:
    if(type(ele) is tuple):
        eleList.extend(list(ele))
    else:
        eleList.append(ele)

element=dict()
freq=list(eleList)
for i in freq:
    element[i]=eleList.count(i)
print("The elements frequency : " + str(element))