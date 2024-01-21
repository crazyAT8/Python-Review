# Arrays
cars = ["Ford", "Volvo", "BMW"]

# Show array
x = cars[0]
print(x)


cars[0] = "Toyota"
y = cars[0]
print(y)

# Get the length
z = len(cars)
print(z)

# Loop through the array
for a in cars:
    print(a)

# Add to the end of Array
cars.append("Honda")
print(cars)

# Remove a specific index
cars.pop(1)
print(cars)

# Remove specific value
cars.remove("Ford")
