class Solution:
    def maxEnvelopes(self, envelopes):
        size = len(envelopes)
        if size < 2:return size

        res = [envelopes[0]]
        for i in range(1,size):
            temp = envelopes[i]
            last = res[-1]
            if temp[0] > last[0] and temp[1] > last[1]:
                res.append(temp)
                continue
            left,right = 0,len(res)-1
            flag = False
            while left < right:
                #找到res中第一个大于信封temp的位置，重新赋值
                mid = (left + right) >> 1
                idx = res[mid]
                if temp[0] > idx[0] and temp[1] > idx[1]:
                    left = mid + 1
                elif temp[0] < idx[0] and temp[1] < idx[1]:
                    # left = mid + 1
                    right = mid
                else:
                    flag = True
                    break
            if not flag:
                res = res[:left] + [temp] + res[left:]

            # res = res[:left] +[temp] + res[left:]
            # res[left] = temp
        print(res)
        return len(res)

if __name__ == "__main__":
    so = Solution()
    nums =  [[5,4],[6,4],[6,7],[2,3]]
    res = so.maxEnvelopes(nums)
    print(res)


