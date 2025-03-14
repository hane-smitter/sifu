"""
Implement an algorithm to determine if a string has all
unique characters.
"""

unique_str = "AbCDefG"
non_unique_str = "non Unique STR"


def is_unique_1(input_str):
    _hash = {}

    for char in input_str:
        if char in _hash:
            return False
        _hash[i] = 1
    return True


def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)


def is_unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True


def normalize_str(input_str):
    input_str = input_str.replace(" ", "")
    return input_str.lower()


unique_str = normalize_str(unique_str)
non_unique_str = normalize_str(non_unique_str)

print(unique_str)
print(non_unique_str)

print(is_unique_1(unique_str))
print(is_unique_1(non_unique_str))

print(is_unique_2(unique_str))
print(is_unique_2(non_unique_str))

print(is_unique_3(unique_str))
print(is_unique_3(non_unique_str))
