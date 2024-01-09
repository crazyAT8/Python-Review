thisdict = {
    "brand": "Ford",
    "color": "red",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

thisdict.pop("model")
print(thisdict)

# removes the last item of the dictionary
thisdict.popitem()
print(thisdict)

# removes the item with the specified name
del thisdict["brand"]

# empties the dictionary
thisdict.clear()
print(thisdict)
