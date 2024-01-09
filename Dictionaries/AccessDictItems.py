exampleDict = {
    "band": "The Faint",
    "Album": "Wet From Birth",
    "TrackNumber": 1,
    "SongName": "Desperate Guys"
}

x = exampleDict["Album"]
print(x)

# or

y = exampleDict.get("TrackNumber")
print(y)

z = exampleDict.keys()
print(z)

a = exampleDict.values()
print(a)

b =exampleDict.items()
print(b)