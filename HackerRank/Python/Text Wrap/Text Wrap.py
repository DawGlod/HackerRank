def wrap(string, max_width):
    new_str = textwrap.wrap(string, max_width)
    new = ""
    for word in new_str:
        new += f"{word}\n"
    return new