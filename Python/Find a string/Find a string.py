def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string) - len(sub_string) + 1):
        word = ""
        for j in range(len(sub_string)):
            word += string[j+i]
        if word == sub_string:
            counter += 1
    return counter