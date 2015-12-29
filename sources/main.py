
def find_next(original, pattern):
    if not pattern:
        raise RuntimeError("Pattern must be supplied")
    elif not isinstance(original, str) or not isinstance(pattern, str):
        raise TypeError("Data type must be str")

    original_length = len(original)
    pattern_length = len(pattern)

    for i in range(original_length - pattern_length):

        flag = True

        for j, character in enumerate(pattern):
            if original[i + j] is not character:
                flag = False

        if flag:
            yield i


if __name__ == "__main__":
    original = "hello world empty set empty world hello"
    pattern = "empty"
    for index in find_next(original, pattern):
        print(index)