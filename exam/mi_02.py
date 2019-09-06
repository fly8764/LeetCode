def find(nums):
    size = len(nums)
    if size == 0:
        return True
    stack = []
    mid = size//2
    left,right = mid,mid
    if size & 1:
        left += 1
    for i in range(left):
        stack.append(nums[i])

    for j in range(right,size):
        temp = stack[-1]
        if temp != nums[j]:
            return False
        stack.pop()

    return True

def find2(nums):
    size = len(nums)
    if size %2 == 0 or size == 1:
        return True
    dp = [0] *size
    for i in reversed(range(size)):
        dp[i] = nums[i]
        for j in range(i+1,size):
            dp[j] = max(nums[i] -dp[j],nums[j]-dp[j-1])
    return dp[-1] > 0


if __name__ == '__main__':
    nums = list(map(int,input().split()))
    res = find2(nums)
    if res:
        print('Yes')
    else:
        print('No')