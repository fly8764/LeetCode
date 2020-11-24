# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        pass

    def search(self,data,k,idx,left,right):
        left_1 = idx -1
        right_1 = idx + 1
        cnt = 1
        while left_1 >= left:
            if data[left_1] == k:
                cnt += 1
                left_1 -= 1
            else: break

        while right_1 <= right:
            if data[right_1]==k:
                cnt += 1
                right_1 += 1
            else: break
        return cnt

    def GetNumberOfK(self, data, k):
        left = 0
        right = len(data)-1

        while left <= right:
            mid = int(left + (right-left)/2)
            tmp = data[mid]
            if tmp == k:
                # cnt = 0
                # for i in range(left,right+1):
                #     if data[i] == k:
                #         cnt += 1
                # return cnt
                return self.search(data,k,mid,left,right)
            else:
                if tmp < k:
                    left = mid + 1
                else:
                    right = mid -1
        return 0


if __name__ == '__main__':
    func = Solution()
    data = [1,2,3,3,3,3,4,5]
    k = 3
    print(func.GetNumberOfK(data,k))