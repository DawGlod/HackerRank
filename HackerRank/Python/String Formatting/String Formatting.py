def print_formatted(number):
    for i in range(number):
        decimal = str(i+1)
        octal = oct(i+1).removeprefix("0o")
        hexadecimal = hex(i+1).removeprefix("0x").upper()
        binary = bin(i+1).removeprefix("0b")
        a = len((bin(number).removeprefix("0b")))
        print(f"{decimal.rjust(a)} {octal.rjust(a)} {hexadecimal.rjust(a)} {binary.rjust(a)}")