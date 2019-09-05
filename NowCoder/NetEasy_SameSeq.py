"""
题目给定a1,a2...an，这样一个长度为n的序列，现在你可以给其中一些元素
加上一个值x（只能加一次），然后可以给另外一些值减上一个值x（只能减一次），
剩下的元素不能再进行操作。问最后有没有可能找到一个值x使所有元素的值相等。

输入：
输入第一行为一个整数k，代表有k个序列(k<100)，接下来有2*k行:
偶数行为一个整数n，代表给定序列的长度(1<=n<=100,000)
奇数行包含n个元素，a1,a2...an，代表序列中的元素(0<=ai<=100,000)

输出：
输出k行，每行一个YES或者NO

输入
1
5
1 3 3 2 1
输出
YES

思路：
有点求平均值的意思，一部分减小，一部分增加，然后看是否相等；
先看数值种类数，当只有一种时，一定可以；两种时，大的减小或小的增大都可以；
当有三类时，看最大，最小值的平均值 是否和中间值相等，
不等的话，就不行，相等就行；
ps：用集合 会减小比较的次数，时间
"""
#16:20 -- 16：59  40mins

def find(nums):

    new = set(nums)
    size = len(new)
    if size > 3:
        return False

    if size == 3:
        big = max(new)
        small = min(new)
        if (big + small) / 2 in new:
# 这里用集合来判断 中间元素是否存在，相比于原始数据会减少搜索量
            return True
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    k = int(input())
    while k:
        k -= 1
        n = int(input())
        nums = list(map(int,input().split()))
        if find(nums):
            print('YES')
        else:
            print('NO')
