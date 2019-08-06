import sys
#not pass


def rev(s):#'1100101'
    new = ''
    for i in range(len(s)):
        if s[i] == '1':
            new += '0'
        else:
            new += '1'

    for i in range(len(new)):
        if new[i] == '1':
            new = new[i:]
            break

    return new

def find(s,t):
    if s == t or s == rev(t):
        return True


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        s = sys.stdin.readline().strip()
        t = sys.stdin.readline().strip()
        if find(s,t):
            print("YES")
        else:
            print("NO")

