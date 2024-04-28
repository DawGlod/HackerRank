# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = input().split(" ")
a = int(a)
b = int(b)
for i in range(a-1):
    if i % 2 != 0:
        word = (".|." * (i))
        new = word.center(b, "-")
        print(new)
welcome = "WELCOME".center(b, "-")
print(welcome)
for i in range(a-1):
    if i % 2 != 0:
        word = (".|." * ((a-1) - i))
        new = word.center(b, "-")
        print(new)