from typing import List # used to add type hint for List

count_x = lambda nums, x: sum(1 for element in nums if element == x)

# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
