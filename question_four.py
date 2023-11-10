# Sample list of dictionaries
dicts_list = [
    {'x': 1, 'y': 2},
    {'x': 3, 'y': 4},
    {'x': 5, 'y': 6},
    {'x': 7, 'y': 8},
    {'x': 5, 'y': 20}
]

# Using next() to find the first dictionary where 'x' equals 5
# Default to an empty dictionary if not found
first_matching_dict = next((item for item in dicts_list if item.get('x') == 5), {})

print(first_matching_dict)
