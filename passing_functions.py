def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

# print(methodception(add_two_numbers))


# lambda = anonymous function
print(methodception(lambda: 35 + 77))


my_list = [13, 56, 77, 484]

# remove the 13 from the list
print(list(filter(lambda x: x != 13, my_list)))


def not_thirteen(x):
    return x != 13

# same thing with named function
print(list(filter(not_thirteen, my_list))

# same thing with list comprehension
print([x for x in my_ist if x != 13])

