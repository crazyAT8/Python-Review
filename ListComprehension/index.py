# Syntax
#           listName = [expression for item in iterable if condition == True]


# Condition
# Want to create a new list of fruits, that have the letter "a" based on the current list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# Altenate and easier way to write this code

fruits2 = ["apple2", "banana2", "cherry2", "kiwi2", "mango2"]

newlist2 = [x for x in fruits2 if "a" in x]

print(newlist2) 

# You want to print all except for the one specified

newlist3 = [x for x in fruits2 if x != "apple2"]

print(newlist3)

# Normal way to loop through a list 

newlist4 = [x for x in fruits]
print(newlist4)

# Iterable
# can be any iterable obj, 
    # like a list, tuple, set, or dictionary

# us range() function to create an iterable

newlist5 = [x for x in range(10)]
print(newlist5)

# now lets add a condition 
# or lets stop the list at a certain number

newlist6 = [x for x in range(10) if x < 5]
print(newlist6)


# Expression
#       is the current item in the iteration
#           but it is also the outcome, 
#               which you can manipulate before it ends up like a list item in the new list

# print the list in all uppercase letters

newlist7 = [x.upper() for x in fruits]
print(newlist7)

# you can also set the outcome to whatever you like
#   or
#       create a new list based on this old list 
#           replacing everything in this list with a given

newlist8 = ['hello' for x in fruits]
print(newlist8)

# expression can also be a condition
#   not like a filter
#       but as a way to manipulate the outcome

newlist9 = [x if x != "banana" else "orange" for x in fruits]
print(newlist9)

        # return the item if it is not banana, if it is banana return orange