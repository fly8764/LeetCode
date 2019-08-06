import  sys
#pass

def find(n,value):
    ret = []
    for item in value:
        ret.append(str(n+1-item))
    return ret


if __name__ == "__main__":
    # while 1:
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    print(type(line))
    # if not line:
    #     break
    num = list(map(int, line.split()))
    res = find(n,num)
    temp = ' '.join(res)
    print(temp)