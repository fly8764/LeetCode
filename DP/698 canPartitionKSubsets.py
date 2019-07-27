class Solution:
    def canPartitionKSubsets(self, nums, k):
        s = sum(nums)
        if s%k != 0:
            return False

        target = s//k


