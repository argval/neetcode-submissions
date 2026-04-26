from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    word_dict = {}
    for i in word:
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] += 1
    return word_dict

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
