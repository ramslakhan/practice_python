if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    #print(list(arr))
    arr.sort()
    max_ele = max(arr)
    for i in arr[::-1]:
        if i < max_ele:
            print(i)
            break




