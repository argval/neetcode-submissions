def get_longer_word(a: str, b: str) -> str:
    if len(a) < len(b):
        return b
    else:
        return a

# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
