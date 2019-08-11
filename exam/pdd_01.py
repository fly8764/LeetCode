import sys


def find(n,nums):
    if n <3 or n > 2999:
        return

    # min_var = 999999
    min_var = float('inf')

    for i in range(n-2):
        sub = nums[i:i+3]
        bia = sum(sub)/3
        var = ((sub[0]-bia)**2 + (sub[1]-bia)**2 + (sub[2]-bia)**2)/3
        min_var = min(min_var,var)

    return min_var


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    nums = list(map(int,line.split()))

    values = sorted(nums)
    res = find(n,values)
    print('%.2f'%res)