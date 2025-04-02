#how does copy() differ from deepcopy()?

import copy
nested_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(nested_list)
deep_copy = copy.deepcopy(nested_list)
nested_list[0][0] = 'X'
print("Original list:", nested_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)