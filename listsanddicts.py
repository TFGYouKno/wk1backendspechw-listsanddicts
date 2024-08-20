#task 1

def create_squares_list(n):
    squares = [i**2 for i in range(1, n+1)]
    return squares
print(create_squares_list(10))

#time complexity: O(n)

#task 2

def merge_sorted_lists(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
print(merge_sorted_lists(list1, list2))

# time complexity: O(n log n)

#task 3

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

dict1 = {
    'pie': 'apple',
    'ice_cream': 'moose tracks',
    'cobbler': 'peach',
    'cake': None
}

dict2 = {
    'dinner': 'turkey',
    'ice_cream': 'vanilla',
    'appetizer': 'soup',
    'cobbler': 'peach'
}

merged = merge_dictionaries(dict1, dict2)
print(merged)

#time complexity: O(n)

#task 4

def find_dictionary_intersection(dict_1, dict_2):
    intersection = {}
    for key in dict_1:
        if key in dict_2 and dict_1[key] == dict_2[key]:
            intersection[key] = dict_1[key]
    return intersection

dict_1 = {
    'pie': 'apple',
    'ice_cream': 'moose tracks',
    'cobbler': 'peach',
    'cake': None
}

dict_2 = {
    'dinner': 'turkey',
    'ice_cream': 'vanilla',
    'appetizer': 'soup',
    'cobbler': 'peach'
}

intersection = find_dictionary_intersection(dict_1, dict_2)
print(intersection)

# time complexity: O(n)