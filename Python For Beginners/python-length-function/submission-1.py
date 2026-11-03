def get_longer_word(a: str, b: str) -> str:
    longer_word = lambda a, b: a if len(a) >= len(b) else b
    return longer_word(a, b)

# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
