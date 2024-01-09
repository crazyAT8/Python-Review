myset = {"apple", "banana", "cherry"}

# used to store multiple items in a single variable
#   
#   - Unchangeable
#                   Note: they may be unchangeable
#                           meaning you cannot change any existing values           (NO EDITING- BC THERE IS NO ORDER)
#                               but you can remove items and add new items          (YOU CAN ADD AND DELETE)
#
#   - Unordered
#                   Note: this means you cannot be sure
#                            in which order the items will appear
#                                    they could show up shuffled/unordered
#                                       they can not be referenced by index of key
#   - Unindexed
#   - No Duplicates allowed
#                   Note: if there happens to be a duplicate value
#                            it will not appear twice
#   - Any DataType
#   - Can have different data types

print(len(myset))
print(type(myset))

# you can create a set with the set() constructor
newSet = set(("John", "Will", "Mike"))

print(newSet)