def concatenate(s1: str, s2: str) -> str:
    s = s1 + s2
    return "Too long!" if len(s) > 10 else s

# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
