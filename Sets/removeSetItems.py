familySet = {"Will", "Lena", "Winnie", "Desi", "Maria", "Clare", "Mark", "John"}
friendSet = {"Ryan", "Tim", "Mel", "Lenaghan", "Mikey"}

familySet.remove("Will")
print(familySet)
# fanilySet.renove("Anna")
# print(familySet)
familySet.discard("Lena")
print(familySet)
familySet.pop()             # remember that sets are unordered so you don't know what item will be removed
print(familySet)

friendSet.clear()
print(friendSet)
del friendSet
print(friendSet)
