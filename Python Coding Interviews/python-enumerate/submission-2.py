from typing import List

def get_index_of_seven(nums: List[int]) -> int:
    if 7 in nums:
        return nums.index(7)
    else:
        return -1

def get_dist_between_sevens(nums: List[int]) -> int:
    try:
        first_occur = nums.index(7)
        for idx, val in enumerate(nums[first_occur + 1:], start=first_occur + 1):
            if val == 7:
                return idx - first_occur
        return -1 
    except ValueError:
        return -1

# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
