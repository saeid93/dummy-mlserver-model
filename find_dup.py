def find_duplicates(lst):
    seen = {}
    duplicates = []
    
    for item in lst:
        if item in seen:
            duplicates.append(item)
        seen[item] = True

    return duplicates

my_list = [1, 2, 2, 3, 4, 4, 5]
duplicate_items = find_duplicates(my_list)
print(duplicate_items)  # Output: [2, 4]



# def find_duplicates(lst):
#     seen = set()
#     duplicates = set()

#     for item in lst:
#         if item in seen:
#             duplicates.add(item)
#         seen.add(item)

#     return list(duplicates)

# my_list = [1, 2, 2, 3, 4, 4, 5]
# duplicate_items = find_duplicates(my_list)
# print(duplicate_items)  # Output: [2, 4]
