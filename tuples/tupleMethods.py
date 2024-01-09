# Tuple Methods
#   1. count() returns the number of times 
#                a specified value occurs in a tuple

aTuple = (1,2,3,4,2,5,23,6,1,56,1,5)

x = aTuple.count(5)
print(x)

#   2. index() searches the tuple
#                for a specified value
#                    and returns the first position 
#                        of where it was found

y = aTuple.index(1)
print(y)