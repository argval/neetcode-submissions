from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    age_list = []
    for keys in age_dict:
        age_list.append(keys)
    return age_list

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    age_values = []
    for keys in age_dict:
        value = age_dict[keys]
        age_values.append(value)
    return age_values

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
