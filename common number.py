def have_common_member(list1, list2):
    return bool(set(list1) & set(list2))

list_a = [1, 2, 3]
list_b = [4, 5, 3]

print(have_common_member(list_a, list_b))

list_c = [7, 8]
print(have_common_member(list_a, list_c))