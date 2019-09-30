class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        prime = [1]*(n)
        prime[0] = prime[1] = 0
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                #使用切片一次性标记完，把对应位置的值设为0
                #这里必须用[0]*len(prime[i*i:n:i])
                #不能直接等于0，左右的数量要相等
                #质数i倍数的值均不是 素数(质数)
                prime[i*i:n:i] = [0]*len(prime[i*i:n:i])
                # for j in range(i*i,n,i):
                #     prime[j] = 0
        return sum(prime)

    def is_prime(self,n):
        if n == 1:
            return False
        if n==2 or n== 3:
            return True
        if n%6!= 1and n%6!=5:
            return False
        s = int(n**0.5)
        for i in range(5,s+1,6):
            if n%i==0 or n%(i+2) ==0:
                return False
        return True


    def prime_de(self,n):
        res = []
        for i in range(2,n):
            while i!=n:
                if n%i == 0:
                    res.append(i)
                    n //=i
                else:
                    break
            if self.is_prime(n):
                res.append(n)
                break
        return res


