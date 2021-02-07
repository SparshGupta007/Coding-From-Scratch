# Author: SPARSH GUPTA
# Program to demonstrate an example of how multiple inputs are taken from end user

# Taking multiple inputs at a time using split
a, b, c = input("Enter 3 values: ").split()
print("The 3 numbers are {}, {}, {}".format(a, b, c))

# Taking multiple inputs at a time using list comprehension
a, b, c = [int(x) for x in input("Enter 3 values: ").split()]
print("The 3 numbers are {}, {}, {}".format(a, b, c))


####################################################################################

# Output :

'''
Enter 3 values: 10 20 30
The 3 numbers are 10, 20, 30

Enter 3 values: 40 50 60
The 3 numbers are 40, 50, 60
'''

####################################################################################

