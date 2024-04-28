if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        cmd, *nums = input().strip().split(' ')
        if cmd == "insert":
            i = int(nums[0])
            e = int(nums[1])
            arr.insert(i, e)
        elif cmd == "print":
            print(arr)
        elif cmd == "remove":
            e = int(nums[0])
            arr.remove(e)
        elif cmd == "append":
            e = int(nums[0])
            arr.append(e)
        elif cmd == "sort":
            arr.sort()
        elif cmd == "pop":
            arr.pop()
        elif cmd == "reverse":
            arr.reverse()