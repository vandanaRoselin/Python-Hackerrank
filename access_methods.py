my_list = [1, 2, 3, 4, 5]

# Append: Add an element to the end of the list
my_list.append([2,5])
my_list[0]=23
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

print(type(my_list))
my_list[0]=23
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])  # Output: 3
#my_tuple[0]=23
print(my_tuple)

my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Adding and updating elements
my_dict['d'] = 4

my_dict['a']=9
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

my_dict.update({'e': 5, 'f': 6})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}