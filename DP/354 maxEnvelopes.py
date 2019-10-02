'''
方法一，错误,如果上来，不按照 宽度或高度排序，直接按照默认的顺序，插入，比较
难以得到最好的结果，即最长上升子序列，比如
[[5,4],[10,5],[6,5],[7,6],[8,7]],
按照默认的顺序，只会得到[[5,4],[10,5]],但是如果去掉中间的[10,5]，会得到更好的结果
[[5,4],[6,5],[7,6],[8,7]]，所以，需要先排序，按照宽度，或高度

方法二：先按照宽度升序排序，再按照高度降序排序，这里有个技巧，
重点 同宽度，高度降序排序，这题类似于 最长上升子序列，值越小，后面可能接的子序列才有可能更长
以避免 [[11, 3], [12, 4], [12, 5], [12, 6], [14, 6]] 这种情况发生
正确排序 [[11, 3], [12, 6], [12, 5], [12, 4], [14, 6]]
同宽度，高度降序排序，上一次，高度较大，这次，来个较小的高度，直接把上次的替换掉，所以，这样就可以保证
同宽度的信封中，只有一个最小高度，非常的方便，不用再写个函数进行判断
'''
class Solution:
    #方法一
    # def maxEnvelopes(self, envelopes):
    #     size = len(envelopes)
    #     if size < 2:return size
    #     res = [envelopes[0]]
    #     for i in range(1,size):
    #         temp = envelopes[i]
    #         last = res[-1]
    #         if temp[0] > last[0] and temp[1] > last[1]:
    #             res.append(temp)
    #             continue
    #         left,right = 0,len(res)-1
    #         flag = False
    #         while left < right:
    #             #找到res中第一个大于信封temp的位置，重新赋值，插到该位置的前面
    #             mid = (left + right) >> 1
    #             idx = res[mid]
    #             if temp[0] > idx[0] and temp[1] > idx[1]:
    #                 left = mid + 1
    #             # elif temp[0] < idx[0] and temp[1] < idx[1]:
    #             else:
    #                 left = mid + 1
    #                 right = mid
    #             # else:
    #             #     flag = True
    #             #     break
    #             # else:
    #             #     flag = True
    #             #     break
    #
    #         while res[left][0] < temp[0] and res[left][1] < temp[1]:
    #             left += 1
    #         if res[left][0] > temp[0] and res[left][1] > temp[1]:
    #             res = res[:left] + [temp] + res[left:]
    #         # res = res[:left] + [temp] + res[left:]
    #
    #         # res = res[:left] +[temp] + res[left:]
    #         # res[left] = temp
    #     print(res)
    #     return len(res)

    #方法二
    def maxEnvelopes(self, envelopes):
        size = len(envelopes)
        if size < 1:return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        tail = [envelopes[0][1]]
        for i in range(1,size):
            temp = envelopes[i][1]
            if temp > tail[-1]:
                tail.append(temp)
                continue
            left,right = 0,len(tail)-1
            while left < right:
                mid = (left+right)>>1
                if tail[mid] < temp:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = temp
        return len(tail)



    def search(self,nums,target):
        size = len(nums)
        if size < 1:return
        left,right = 0,size
        while left < right:
            mid = (left + right)>>1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        #找到第一个大于目标值的索引
        while nums[left] <= target:
            left += 1

        return left


if __name__ == "__main__":
    so = Solution()
    # nums = [[5,4],[6,4],[6,7],[2,3]]
    nums = [[5,4],[10,5],[6,5],[7,6],[8,7],[9,8]] #特例
    res = so.maxEnvelopes(nums)
    print(res)
    # target = 4
    # nums = [1,2,3,5,9]
    # print(so.search(nums,target))


