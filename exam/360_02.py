def find(arr,n):
    size = len(arr)

    maxx = 0

    for i in range(size):
        temp = 0
        while temp <= n and i < size:
            temp += arr[i]
            if temp >n:
                break
            maxx = max(temp,maxx)
            i += 1

    return maxx

if __name__ == '__main__':
    line = list(map(int,input().split()))
    n,m = line[0],line[1]
    arr = []
    while m:
        m -= 1
        arr.append(int(input()))

    res = find(arr,n)
    print(res)