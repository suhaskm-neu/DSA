# Creating an array
my_array = [1, 2, 3, 4, 5]

# Accessing elements in an array
first_element = my_array[0]
last_element = my_array[-1]

# Modifying elements in an array
my_array[2] = 10

# Finding the length of an array
array_length = len(my_array)

# Adding elements to an array
my_array.append(6)
my_array.insert(0, 0)

# Removing elements from an array
removed_element = my_array.pop()
removed_element = my_array.pop(2)
my_array.remove(4)

# Sorting an array
my_array.sort()

# Reversing an array
my_array.reverse()

# Copying an array
new_array = my_array.copy()

# Checking if an element exists in an array
element_exists = 3 in my_array

# Finding the index of an element in an array
element_index = my_array.index(2)

# Counting the occurrences of an element in an array
element_count = my_array.count(2)

# Slicing an array
sliced_array = my_array[1:4]