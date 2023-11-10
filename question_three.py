# Sample list of integers
integers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension with a lambda function to filter even numbers
even_integers = list(filter(lambda x: x % 2 == 0, integers_list))

print(even_integers)