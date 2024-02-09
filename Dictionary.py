# Problem-1
# Write a Python program for dictionary print all duplicates charecters.

# Example 1
# Input : 'aadidimri'
# Output : a d i

# Code: 
 
def find_dup_char(input):
    x=[]
    for i in input:
        if i not in x and input.count(i)>1:
            x.append(i)
    print(" ".join(x))
 
if __name__ == "__main__":
    input = 'aadidimri'
    find_dup_char(input)


# Problem-2
# Write a Python program for dictionary to print a user given persone Name, Shoes size & Age.
    
# Example 2
# Input : user given
        # How may person entery you want to do : 2
        # Enter the person name : Mohit
        # Enter the person shoes size  : 7
        # Enter the person age : 23
        # Enter the person name : Aadi
        # Enter the person shoes size  : 8
        # Enter the person age : 23
# Output : Person => Name: Mohit ,Age: 23 ,Shoesize: 7
#          Person => Name: Aadi ,Age: 23 ,Shoesize: 8
    
# Code
    
user={}
number_person=int(input('How may person entery you want to do : '))
for i in range(0,number_person):
    personName=input('Enter the person name : ')
    personshoesSize=int(input('Enter the person shoes size  : '))
    personAge=int(input('Enter the person age : '))

    user[personName]={'age':personAge,'shoesSize':personshoesSize}
for personName in user:
    print('Person => Name:',(personName),',Age:',user[personName]['age'],',Shoesize:',user[personName]['shoesSize'])