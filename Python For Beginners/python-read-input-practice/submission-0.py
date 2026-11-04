def add_two_numbers() -> int:
    line = input()
    num_string = line.split(",")
    num_list = []
    sum = 0

    for s in num_string:
        sum += int(s)

    return sum


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
