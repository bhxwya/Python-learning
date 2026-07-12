'''Takes Time'''
# my_list = []
# for i in range(0, 201):
#     my_list.append(i)
# print(my_list)


'''Same thing but takes less and is in cleaner syntax'''
# my_list = [i for i in range(0, 201)]
# print(my_list)


# 0+6 = 6, 1+6=7, 2+6=8....... 20+6=26 stops
# my_list = [i + 6 for i in range(0, 21)]
# print(my_list)


# my_list = ["even" for i in range(0, 21)]
# print(my_list)


# my_list = [i % 2 for i in range(0, 21)]
# print(my_list)


# whenn u have two conditions
# my_list = ["EVEN" if i % 2 == 0 else "ODD" for i in range(1, 21)]
# print(my_list)


'''when you have only one condition  (u can't use IF in front bcs there's no condition to put
in else) so add in back it will work without syntax error'''
# example print (2,4,6,8....)

# my_list = [i if i % 2 == 0 for i in range(1, 51)] #gives error
my_list = [i for i in range(1, 51) if i % 2 == 0] #works
print(my_list)
