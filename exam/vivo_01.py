def solution(nums):
    size = len(nums)
    if size < 1:return -1
    if size < 2:
        return 0
    dp = [float('inf')]*size
    # for i in range(size):
    #     dp.append(i)
    dp[0] = 0
    for i in range(1,size):
        # cnt = 0
        for j in range(i-1,-1,-1):
            if nums[j] >= i-j and dp[j] + 1 < dp[i]:
                dp[i] = dp[j]+1
                # cnt += 1
        # if i > 0 and not cnt:return -1
        if dp[i] == float('inf'):
            return -1
    return dp[-1]

step_list = [int(i) for i in input().split()]
print(solution(step_list))