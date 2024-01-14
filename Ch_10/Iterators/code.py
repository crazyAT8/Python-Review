# Iterator vs Iterable

myTuple = ("apple", "banana", "cherry")
myIt = iter(myTuple)

print(next(myIt))
print(next(myIt))
print(next(myIt))

myStr = "banana"
myIt2 = iter(myStr)

print(next(myIt2))
print(next(myIt2))
print(next(myIt2))
print(next(myIt2))
print(next(myIt2))
print(next(myIt2))

# Looping Through an Iterator

myTuple2 = ("apple", "banana", "cherry")

for x in myTuple2:
    print(x)

myStr2 = "banana"

for x in myStr2:
    print(x)