# Python Conditions and If statements

a = 33
b = 200
if b > a:
    print("b is greater than a")

# Elif

c = 33
d = 33
if d > c:
    print("d is greater than c")
elif c == d:
    print("c and d are equal")

# Else

e = 200 
f = 33
if f > e:
    print("f is greater than e")
elif e == f:
    print("e and f are equal")
else:
    print("e is greater than f")


# Short Hand If

g = 200
h = 33

if g > h: print("g is greater than h")

if g > h:
    print("g is greater than h")


# Short Hand If ... Else

i = 2
j = 330

print("I") if i > j else print("J")

if i > j:
    print("I")
else:
    print("J")


# Multiple 'else' statements on the same line

k = 330
l = 330

print("K") if k > l else print("=") if k == l else print("L")

if k > l:
    print("K")
elif k == l:
    print("=")
else:
    print("L")


# And

a2 = 200
b2 = 33
c2 = 500

if a > b and c > a:
    print("Both conditions are True")


# Or

a3 = 200
b3 = 33
c3 = 500

if a > b or a > c:
    print("At least on of the conditions is True")


# Not

a4 = 33
b4 = 200

if not a4 > b4:
    print("a is NOT greater than b")

# Nested if statement

x = 39

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20!")


# the pass statement

a5 = 33
b5 = 200

if b5 > a5:
  pass

# having an empty if statement like this, would raise an error without the pass statement