arr = [1, 2, 3, 4, 5, 6, 7]


def find(arr, ans):
    pos = int(len(arr) / 2)
    while 0 <= pos < len(arr):
        if (arr[0] == ans):
            return 0
        if (arr[pos] == ans):
            print(pos)
            return pos
        elif arr[pos] > ans:
            print(pos)
            pos = pos - int(len(arr[:pos]) // 2)
        elif arr[pos] < ans:
            print(pos)
            pos = pos + int(len(arr[pos:]) // 2)


    return -1


print(find(arr, 6))