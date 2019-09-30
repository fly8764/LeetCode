class Solution():
    def prime_de(self,n,table):
        res = []
        for i in range(2,n+1):
            while(i!= n):
                if n%i == 0:
                    res.append(i)
                    n //= i
                else:break
            if table[n]:
                res.append(n)
                break
        return len(res)

    def find(self,n):
        table = [1]*n
        table[0] = table[1] = 0
        cnt = 0

        for i in range(2,n):
            if table[i]:
                for j in range(i*i,n,i):
                    table[j] = 0

        for i in range(2,n):
            if not table[i]:
                temp = self.prime_de(i,table)
                # print(i,temp)
                cnt += temp
                # cnt += self.prime_de(i)
            else:
                cnt += 1
        return cnt


if __name__ == "__main__":
    so = Solution()
    n = int(input())
    # print(so.prime_de(n))
    print(so.find(n+1))