this = ("apple", "banana", "cherry")

print(this) 



# Tuple Updates
                # tuples are immutable/unchangable
                # meaning you can not add, remove or replace anything
                    # but there is always a work around

x = ("apple", "banana", "cherry")       # create a tuple
y = list(x)                             # convert the tuple to a list
y[1] = "kiwi"                           # replace a numbered index with something new
x = tuple(y)                            # comvert back to a list

print(x)                                 # show the new version of the tuple 


                                            # Add Items to a Tuple

thistuple = ("apple", "banana", "cherry")
a = list(thistuple)
a.append("orange")
thistuple = tuple(a)

print(thistuple)



                                            # Adding a Tuple to another Tuple 
                                                    # this proccess is absolutely aloud

thistuple += this 

print(thistuple)



                                                # Remove Items

b = list(thistuple)
b.remove("orange")
thistuple = tuple(b)

print(thistuple)



                                                 # Delete Tuple Completely

# del thistuple

# print(thistuple)
                        # which will raise an error bc the tuple no longer exists


                                                # Unpack Tuples
names = ("Will", "John", "Mike")
    # pack the tuple
(A, B, C) = names 
    # assign a series of variables to the name of the tuple
    # the number of variables must corrispond with the number of values within the tuple

print(A)
print(B)
print(C)

                                # Using Asterick*
        # If the number of variables is less than the number of values
        # you can add an * to the variable name 
        # and the values will be assigned to the variable as a list

colors = ("red", "black", "green", "blue", "white")

(D, E, *F) = colors 

print(D)
print(E)
print(F)


        # if the asterick is added to another variable name than the last
        # python will assign values to the variable 
            # until the number of values left 
            # matches the number of variables left

brothers = ("ryan", "declan", "josh", "Nick", "Max")

(G, *H, I) = brothers 

print(G)
print(H)
print(I)