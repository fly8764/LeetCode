'''
考虑各种边界条件，case
数字必须连续，后面一旦中断，后面的就不算了
前面如果有正负号，也必须和后面的数字连续
处理顺序：
空格、正负号、非数字字符（res长度是否为0），正常的字符
'''
class Solution:
    def myAtoi1(self, s):
        size = len(s)
        neg = False
        res = ''
        dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        for i in range(size):
            if s[i] == ' ':
                continue
            if s[i] == '-':
                neg = True
                if i < size -1 and s[i+1] not in dic:
                    return 0
                continue
            if s[i] == '+':
                if i < size -1 and s[i+1] not in dic:
                    return 0
                continue
            #在遇到数字字符前遇到非空格或负号以外的字符，比如字母字符
            if s[i] not in dic:
                if len(res) == 0:return 0
                else:break

            if len(res) == 0 and s[i] not in dic:
                return 0
            if '0'<= s[i] <= '9':
                res += s[i]
                if i < size -1 and s[i+1] not in dic:
                    break
                continue
            # if len(res) > 0 and s[i] not in dic:
            #     break
        ans = 0
        mod = 10
        for i in range(len(res)):
            ans *= mod
            ans += dic[res[i]]
        if neg:
            ans *= -1
        if ans > (1<<31)-1:
            return (1<<31)-1
        if ans < -1*(1<<31):
            return -1*(1<<31)
        return ans

    # def myAtoi(self, s: str) -> int:
    #     return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


if __name__ == '__main__':
    so = Solution()
    # print(so.myAtoi("42"))
    # print(so.myAtoi("   -42"))
    # print(so.myAtoi("4193 with words"))
    # print(so.myAtoi("words and 987"))
    # print(so.myAtoi("-91283472332"))
    # print(so.myAtoi("0.14159"))
    # print(so.myAtoi("+1"))
    # print(so.myAtoi("+-1"))
    # print(so.myAtoi("+0 123"))
    print(so.myAtoi("2147483646"))

