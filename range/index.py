'''
In Python, 
    range is a built-in function that generates a sequence of numbers. 
    It is commonly used in loops to iterate over a sequence of numbers. 
    The range function can take one, two, or three arguments:

1. start (optional): the starting point of the sequence (default is 0).
2. stop: the endpoint of the sequence (not included in the range).
3. step (optional): the difference between each number in the sequence (default is 1).

For example, range(3) will generate 0, 1, 2, 
                and range(2, 5) will generate 2, 3, 4. 
    
    It's a versatile and commonly used tool in Python 
        for controlling the flow and number of iterations in loops.

'''



# 1. Generate numbers from 0 to 4
for i1 in range(5):
    print(i1)

# 2. Generate numbers from 1 to 4
for i2 in range(1, 5):
    print(i2)

# 3. Generate numbers from 1 to 9, incrementing by 2
for i3 in range(1, 10, 2):
    print(i3)



''' 
You replace the numbers with your desired start, stop, and step values. 
    The range function is often used in for loops 
        to repeat an action a certain number of times 
        or to iterate through sequences by index.
'''