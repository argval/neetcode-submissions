def print_string_characters(word1: str, word2: str) -> None:
    list_word = [word1, word2]
    for word in list_word:
        len_word = len(word)
        for i in range(len_word):
            print(word[i])

# do not modify below this line
print_string_characters("Hello, World!", "Good Job!")
