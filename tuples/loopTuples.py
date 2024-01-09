# you can loop through a tuple with a for loop

aTuple = ("apple", "banana", "cherry")
for x in aTuple:
    print(x)

# Loop Through the Index Numbers
#   you can also loop through the tuple items
#       by referring to their index number
# use the range() and len() functions
#   to create a suitable iterable

aTuple2 =("peach", "rasberry", "strawberry")
for i in range(len(aTuple2)):
    print(aTuple2[i])

# Using a While Loop
#   len() function to determine the length of the tuple
#        then start at 0 and loop your way through
#           the tuple items by refering to their indexes
#               remember to increase the index by 1 after each iteration

aTuple3 = ("Bill", "Ted", "Jay", "Silent Bob")
j = 0
while j < len(aTuple3):
    print(aTuple3[j])
    j = j + 1