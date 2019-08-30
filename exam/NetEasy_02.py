'''
原文链接：https://blog.csdn.net/qq_17550379/article/details/98514359

小易有一个长度为n的数字数组a1,a2,...an a_1,a_2,...a_na
问你是否能用这n个数字构成一个环（首尾相连），使得环中的每一个数字都小于它相邻的两个数字的和（每个数字都必须使用并且只能使用一次）。

输入描述：
第一行包含一个整数t(1 <= t <= 10)，表示测试用例的组数。
每个测试用例输入如下：
第一行一个整数n，表示数字的个数；
第二行n个整数a1,a2,...an，每两个整数之间用一个空格分隔。
输入数据保证
3 <= n <= 10^5
1 <= ai <= 10^9

输出描述：
输出应该包含t行，对于每组用例，若能则输出"YES"，否则输出"NO"

示例1：
1
5
17 6 17 11 17

输出：YES

示例2：
1
3
1 2 4

输出：NO

思路：
先排序
a1<= a2 <= a3 <= ... <= an-1 <= an
这样 由于 ai < a(i+1),所以 ai<(a(i+1)+a(i-1))，但是对于 an 最后一项，最大，没有哪一个元素能管住他，
所以往前交换一个，让 a(n-1),a(n-2)来求和 大于他，这两个是仅次于an的，所以，最有可能满足要求；至此，就可以检测了

这感觉有技巧在里面，不容易 想到
'''
import sys


t = int(input())
while t:
    n = int(input())
    data = list(map(int, input().split()))
    # data = list(map(int, sys.stdin().readline().strip().split()))
    print(data)
    data.sort()
    data[-1], data[-2] = data[-2], data[-1]
    for i in range(n):
        pre, pos = (i - 1 + n)%n, (i + 1) % n
        if data[i] >= data[pre] + data[pos]:
            print("NO")
            break
    else:
        print("YES")
    t -= 1