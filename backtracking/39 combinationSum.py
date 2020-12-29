class Solution(object):
    def combinationSum(self, nums, target):
        n = len(nums)
        if n < 1:return []
        nums.sort()

        res = []
        def backTrack(nums,tmp,target1):
            if target1 == 0:
                res.append(tmp)
                return

            for i in range(len(nums)):
                item = nums[i]
                # 升序序列，当最小值大于目标值时，可以终端该支路。
                if item > target1:
                    return
                '''
                不使用nums[i]数据的情况不需要像下面这样单独列出来，
                同时这种单独拎出来讨论会报错。
                因为相当于本次循环，什么都没有改变，会无线循环下去。
                想不使用，for循环迭代到下一个值时，如i+1不就不使用i了嘛
                '''
                # backTrack(nums[i:], tmp[:], target1)
                # 如果目标值为负，则中断该支路。
                if target1 < 0:return
                '''
                下面的搜索中，在i及之后的序列中搜索，不能再用i之前的了。
                下一层的递归中如果想用i之前的值，其实已经在该层及上几层用过了。
                '''
                backTrack(nums[i:],tmp+[item],target1-item)

        backTrack(nums,[],target)
        return res


if __name__ == '__main__':
    func = Solution()
    nums,target = [2,3,6,7],7
    # nums,target = [2,3,5],8
    print(func.combinationSum(nums,target))

