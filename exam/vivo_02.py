'''
Welcome to vivo !
给员工编号，员工站一排，从左到右依次报号，当报到最右边时，回到最边继续报号，号码不中断
当号码n是N的整数倍时，该员工出队，
输出一个数组，从左到右代表先后出队的员工的位置下标

思路：
从左到右依次报数，当到达最右边时，再回到最左边，依次可以多次重复for循环，从数组的左边到右边；
for循环的外层是 while循环，终止条件是 所有的员工都出队；
对应 报号满足要求的位置，对应的值置为0，其他的位置的值都对应下标值，
因此，在考虑 每个位置的 报号时，要先判断这个位置是否已经出队（位置上的值为0）；没出队，
则号码m加1，m+1；同时判断m+1是否满足报号要求；
T(n) = n*2
'''
# def solution(N, M):
#  初始解法：报号 理解错误，认为报号报到最右边，就回到左边，又从0开始报号，
#  实际上，号码不会中断
#     res = []
#     nums = []
#     for i in range(N+1):
#         nums.append(i)
#
#     while len(nums) > M:
#         size = len(nums)
#         j = 1
#         copy =[0]
#         while j*M <= size -1:
#             res.append(nums[j*M])
#             copy.extend(nums[(j - 1) * M+1:j * M])
#             j += 1
#         if 0<size - (j-1)*M < M:
#             copy.extend(nums[(j-1)*M+1:])
#         nums = copy[:]
#
#     return res+nums[1:]
def solution(N, M):
    if N < 1: return
    cnt = 0
    res = []
    nums = []
    for i in range(1, N + 1):
        nums.append(i)

    j = 0
    while cnt != N:
        for i in range(N):
            if nums[i] != 0:
                j += 1
                if j % M == 0:
                    res.append(nums[i])
                    cnt += 1
                    nums[i] = 0
    return res

N, M = [int(i) for i in input().split()]
# print(N,M)
print(solution(N, M))
