# -*- coding:utf-8 -*-
'''
in place 方法
题目中给出了条件，n各数字，范围在[0,n-1]之间，因此可以把各个数字放在对应的下标位置，
如果出现 numbers[i] == numbers[numbers[i]]的情况，则找到了第一个重复数字；
这种方法理论上有效，但是实际通过不了。
'''

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    # def duplicate(self, numbers, duplication):
    #     dic = {}
    #     for i in range(len(numbers)):
    #         tmp = numbers[i]
    #         if tmp not in dic:
    #             dic[tmp] = 1
    #         else:
    #             duplication[0] = tmp
    #             return True
    #     return False

    def duplicate(self, numbers, duplication):
        for i in range(len(numbers)):
            while i != numbers[i]:
                if numbers[i] != numbers[numbers[i]]:
                    tmp = numbers[i]
                    numbers[i] = numbers[tmp]
                    numbers[tmp] = tmp

                    # tmp = numbers[numbers[i]]
                    # numbers[numbers[i]] = numbers[i]
                    # numbers[i] = tmp
                else:
                    duplication[0] = numbers[i]
                    return True
        return False


if __name__ == '__main__':
    func = Solution()
    numbers = [0,1,1]
    duplication = [0]
    print(func.duplicate(numbers,duplication))