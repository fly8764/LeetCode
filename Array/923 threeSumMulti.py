class Solution:
    def threeSumMulti(self, nums, target):
        map = {}
        cnt = 0
        for item in nums:
            if item in map:
                map[item] += 1
            else:
                map[item] = 1

        for i,x in map.items():
            for j,y in map.items():
                k = target - i - j
                if k not in map:
                    continue
                z = map[k]
                if i == j == k:
                    cnt += x*(x - 1)*(x-2)//6
                elif i == j != k:
                    cnt += z*x*(x-1)//2
                elif i < j and j < k: #这里要加上限制条件，限制了排列 顺序，就不会有 三个位置的数 各种排列的出现
                # elif i!=j and j!= k: #这种限制条件也不行，因为涉及到三个不同的值之间的排列，所以会重复记录
                    cnt += x*y*z
                cnt %= (10**9 + 7)

        return cnt

if __name__ == '__main__':
    so = Solution()
    nums = [1,1,2,2,3,3,4,4,5,5]
    target = 8
    res = so.threeSumMulti(nums,target)
    print(res)
