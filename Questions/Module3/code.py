# 15
''' 

What is the output?
    o 6 *
    o 7
    o 02
    o 4

'''

# t = [[3 - i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
    # print(t[i][i])
    # s += t[i][i]
    # print(t[i])

# print(s)
# print(t)

# a = [3-i for i in range(3)]
# print(a)


# 16
''' 

What is the output?
    o [1, 1, 1, 1, 2, 3] *
    o [3, 2, 1, 1, 2, 3]
    o [1, 2, 3, 1, 2, 3]
    o [1, 2, 3, 3, 2, 1]

'''


# my_list = [1, 2, 3]
# print(len(my_list))
# for v in range(len(my_list)):
#     # print(v)
#     print(my_list[v])
#     my_list.insert(1, my_list[v])
# print(my_list)


# 17

''' 
After execution of the following snippet,
the sum of all "vals" elements 
will be equal to:
'''
# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
# print(vals)

'''  
 What would the code be to loop through
 the list to add up all of the values
 '''

# total = 0
# for val in vals:
#     total += val 

# print("Sum of all elements:", total)


#18 
'''  
What is the output:
    o [1, 1, 1]
    o [1, 2, 3]
    o [3, 3, 3]
    o [3, 2, 1]
'''

# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v) 
# print(my_list_2)

vals2 = [0,1,2]
vals2[0], vals2[2] = vals2[2], vals2[0]

print(vals2)