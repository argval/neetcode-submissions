from typing import Dict

def print_dict(my_dict: Dict[str, int]) -> None:
    print(my_dict)

def print_value(key: str, my_dict: Dict[str, int]) -> None:
    if key in my_dict:
        print(my_dict[key])

def key_present(key: str, my_dict: Dict[str, int]) -> None:
    if key in my_dict:
        return True
    else:
        return False

def change_value(key: str, value: int, my_dict: Dict[str, int]) -> None:
    if key in my_dict:
        my_dict[key] = value

    else:
        print("Key entered not present in the dictionary")

your_dict = { 
  "a": 10, 
  "apple": 12,
  "bat": 7
}

print_dict(your_dict)
print_value("a", your_dict)
print(key_present("d", your_dict))
change_value("a", 4, your_dict)
print_dict(your_dict)