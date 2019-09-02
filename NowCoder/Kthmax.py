# def find(nums):
#     new = sorted(nums,reverse = True)
#     # new_ = set(new)
#     res = 0
#     for i in range(3):
#         res = new_.pop()
#     return res

if __name__ == '__main__':
    line = input()
    line = line.replace('[','').replace(']','').split(',')
    # nums = eval(input().strip())
    # print(line,type(line))
    # line = line[1:-1]
    nums = list(map(int,line))
    # nums = map(int,line)
    # print(nums)
    nums.sort()
    print(nums[-3])

