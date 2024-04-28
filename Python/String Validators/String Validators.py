def checker_a(word):
    for c in word:
        if c.isalnum():
            return True
    return False


def checker_b(word):
    for c in word:
        if c.isalpha():
            return True
    return False


def checker_c(word):
    for c in word:
        if c.isdigit():
            return True
    return False


def checker_d(word):
    for c in word:
        if c.islower():
            return True
    return False


def checker_e(word):
    for c in word:
        if c.isupper():
            return True
    return False


if __name__ == '__main__':
    s = input()
    print(checker_a(s))
    print(checker_b(s))
    print(checker_c(s))
    print(checker_d(s))
    print(checker_e(s))