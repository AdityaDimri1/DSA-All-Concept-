# Problem-1
# Write a Python program to swap first and last element of the list.

# Examples: 
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Code:-
numberList=[]                          # This block of code used in all the programs for taking user input
numberOfEntry=int(input('Enter the number of entry: ')) # and store it into a list.
for entery in range(0,numberOfEntry):
    userInput=int(input('Enter the number : '))
    numberList.append(userInput)

size=len(numberList)
temp=numberList[0]
numberList[0]=numberList[size-1]
numberList[size-1]=temp
print(numberList)


# Problem-2
# Write a Python program to Sum of number digits in List.

# Example:
# Input: [12, 67, 98, 34]
# Output: [3, 13, 17, 7]

# Code:
numberList=[12, 67, 98, 34]
digitSumList=[]
for num in numberList:
    sum=0
    for digit in str(num):
        sum+=int(digit)
    digitSumList.append(sum)
print(digitSumList)