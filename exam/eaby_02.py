n = int(input())
nums = list(map(int,input().split()))
m = int(input())

res = []
for i in range(m):
    l,r = list(map(int,input().split()))
    dic = {}
    for num in nums[l-1:r]:
        if num in dic.keys():
            dic[num] +=1
        else:
            dic[num] = 1
    cnt = 0
    for key in dic.keys():
        if dic[key] == 1:
            cnt += 1
    res.append(cnt)

for r in res:
    print(r)