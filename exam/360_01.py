import sys

def find2(s):
    size = len(s)
    dic = {}
    for i in range(size):
        sub = s[i]
        if sub not in dic:
            dic[sub] = 1
        else:
            dic[sub] += 1
    maxx = 1
    # print(dic)
    for key,val in dic.items():
        maxx = max(val,maxx)

    return maxx


def find(s):
    size = len(s)

    dic = {}
    for l in range(1,size):
        for i in range(size-l+1):
            sub = s[i:i+l]
            if sub not in dic:
                dic[sub] = 1
            else:
                dic[sub] += 1
    maxx = 1
    # print(dic)
    for key,val in dic.items():
        maxx = max(val,maxx)

    return maxx

if __name__ == '__main__':
    s = input()
    res = find2(s)
    print(res)