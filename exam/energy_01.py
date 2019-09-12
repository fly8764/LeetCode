def find(nums):
    size = len(nums)
    nums = nums[::-1]

    dp_0 = 0
    dp_1 = float('-inf')

    for i in range(size):
        temp= dp_0
        dp_0 = max(dp_0,dp_1 + nums[i])
        dp_1 = max(dp_1,temp - nums[i])

    return dp_0


if __name__ == '__main__':
    nums = list(map(int,input().split(',')))
    res = find(nums)
    print(res)