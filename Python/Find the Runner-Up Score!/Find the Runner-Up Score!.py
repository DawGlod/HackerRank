if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 2:
        first = max(arr)
        second = min(arr)
    elif n > 2:
        first = max(arr)
        second = min(arr)
        for i in range(n):
            if second < arr[i] < first:
                second = arr[i]
            elif arr[i] > arr[i]:
                second = first
                first = arr[i]
    print(second)