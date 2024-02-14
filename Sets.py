# Problem-1
# Write a Python program for demonstrate union of two sets using union() function or | operator.

# Example 
# Input :  people = {"Jay", "Idrish", "Archil"}
#          vampires = {"Karan", "Arjun"}
#          dracula = {"Deepanshu", "Raju"}
# Output : Union using union() function
#          {'Archil', 'Idrish', 'Arjun', 'Karan', 'Jay'}   
#          Union using '|' operator
#          {'Archil', 'Idrish', 'Deepanshu', 'Raju', 'Jay'}

# Code :

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
 
# Union using union() function

population = people.union(vampires) 
print("Union using union() function")
print(population)
 
# Union using "|" operator

population = people|dracula
print("Union using '|' operator")
print(population)


# Problem-2
# Write a Python program to demonstrate differences between two sets.

# Example 
# Input :  {0, 1, 2, 3, 4}
#          {3, 4, 5, 6, 7, 8}
# Output :  Difference of two sets using difference() function
#           {0, 1, 2}
#           Difference of two sets using '-' operator
#           {0, 1, 2}

# Code :

set1 = set()
set2 = set()
 
for i in range(5):
    set1.add(i)
 
for i in range(3,9):
    set2.add(i)
 
# Difference of two sets using difference() function
    
set3 = set1.difference(set2)
print("Difference of two sets using difference() function")
print(set3)
 
# Difference of two sets using '-' operator

set3 = set1 - set2
print("Difference of two sets using '-' operator")
print(set3)