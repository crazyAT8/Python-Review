# How to Add to a Set
setEx = {"Mr. Blue", "Mr. Brown", "Mr. Pink"}

setEx.add("Mr. Blonde")

print(setEx)

# How to add a Set to a Set
setEx2 = {"Mrs. Black", "Mrs. Blue", "Mrs. Green"}

setEx.update(setEx2)

print(setEx)

# Note that you can add an Array/Iterable Obj of any kind to a Set
#       but it will return a set

listEx = ["Mr.Turqoise", "Mrs. RedRaspberry"]

setEx.update(listEx)

print(setEx)