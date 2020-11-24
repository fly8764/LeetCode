# -*- coding:utf-8 -*-
'''
方法一 使用两个辅助数组：
遍历一遍，分成奇偶两组，最后拼接在一块，输出；
T(n) = O(n) O(n) = o(n)

方法二 冒泡法：
遇到偶数在前，奇数在后的数据，交换位置。相反的或其它情形的不改变。
这样有两层循环，T(n)=o(n^2),但是O(n)=o(l)

'''
class Solution:
    def reOrderArray(self, array):
        odd = []
        even = []
        for i in range(len(array)):
            if array[i]%2 == 0:
                even.append(array[i])
            else:
                odd.append(array[i])
        return odd + even

if __name__ == '__main__':
    func = Solution()
    array = [1,3,10,8,7,4,5,6]
    print(func.reOrderArray(array))