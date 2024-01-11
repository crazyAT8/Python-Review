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


my_list = [1, 2, 3]
print(len(my_list))
for v in range(len(my_list)):
    # print(v)
    print(my_list[v])
    my_list.insert(1, my_list[v])
print(my_list)

