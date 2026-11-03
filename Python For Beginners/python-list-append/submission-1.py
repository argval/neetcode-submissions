from typing import List # this is used to add type hints for List type

append_to_list = lambda my_list, elements: [*my_list, *elements]

# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
