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


# Create an Iterator

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self 

    def __next__(self):
        x = self.a 
        self.a += 1
        return x

myclass = MyNumbers()
myIter3 = iter(myclass)

print(next(myIter3))
print(next(myIter3))
print(next(myIter3))
print(next(myIter3))
print(next(myIter3))


# StopIteration

class MyNumbers2: 
    def __iter__(self):
        self.a = 1
        return self 

    def __next__(self):
        if self.a <= 20:
            x = self.a 
            self.a += 1
            return x
        else:
            raise StopIteration 

myclass2 = MyNumbers2()
myIter4 = iter(myclass2)

for x in myIter4