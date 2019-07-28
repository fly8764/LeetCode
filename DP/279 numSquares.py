class Solution:

    def numSquares(self,n):
        #BFS
        pass

    _dp = [0]
    def numSquares3(self,n):
        #改进的dp，加入了类属性
        # f(n) = min(f(n - num1), f(n - num2), ... , f(n - numx)) + 1
        # 这里是一个trick，把_dp变成一个类属性，这样这个类的所有对象都可以访问，共享这个属性，
        # 因为测试用例有很多的重复计算

        dp = self._dp
        while len(dp) <= n:
        #dp动态的添加，list的后面有个逗号， ，这个逗号是建立元组tuple,(9,),然后list((9,))
        #从后往前计算，每次遍历的i为 int(len(dp)**0.5)+1)，不会超出界限
            dp += list((min(dp[-i*i] for i in range(1,int(len(dp)**0.5 +1)))+1,))
        return dp[-1]

    def numSquares2(self,n):
        #原始dp超时
        max_num = int(n**0.5)+1
        nums = [i*i for i in range(1,max_num)]

        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1]= 1
        dp += list((min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,))

        for i in range(2,n+1):
            for num in nums:
                if i >= num:
                    dp[i] = min(dp[i],dp[i-num]+1)
                else:
                    break
        return dp[-1]

    def numSquares1(self, n):
        # 四平方定理
        # Lagrange's Four Square theorem：
        # 每个正整数均可表示为4个整数（包括0）的平方和，
        # 所以只有四种可能结果，即[1,2,3,4]
        # Legendre's three-square theorem：
        # 非4^a(8b+7)型的正整数都可以用三个整数的平方和表示，
        # 所以对于可以写成4^a(8b+7）类型的n，其结果只能为4
        # https://blog.csdn.net/qq_17550379/article/details/80875782
        while n%4 == 0:
            n /= 4
        if n % 8== 7:
            return 4

        a = 0
        while a*a <= n:
            b = int((n- a*a)**0.5)
            if a*a + b*b == n:
                return (not not a) + (not not b) #新技能，get！！！
            a += 1
        return 3

if __name__ == '__main__':
    so = Solution()
    res = so.numSquares(1)
    print(res)


