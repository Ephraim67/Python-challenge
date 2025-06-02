def longest_value(d: dict):
    """Using a dictionary, find the longest value."""
    if not d:
        return None
    
    longest_key = max(d, key=lambda k: len(d[k]))
    return d[longest_key]

fruits = {'fruit': 'apple', 'color': 'green'} 
print(longest_value(fruits))

# def first_longest_value(data_dict):
#     # Initialize variables to keep track of the longest value
#     longest_value = ""
    
#     for value in data_dict.values():
#         if len(value) > len(longest_value):
#             longest_value = value
#     return longest_value
