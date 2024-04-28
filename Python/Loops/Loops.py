if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        if i >= 0:
            nums.append(i)
    result = list(map(lambda x: x*x, nums))
    print(*result, sep="\n")