'''
使用栈，先进后出
左括号依次入栈，遇到右括号时，使用栈顶元素，即最近的左括号，
和其比较配对，如果配对，则消去栈顶元素，最近的左括号。
这样就不用为每种括号单独设置一个累计值，而其累计值的方法行不通。
最后，观察栈是否为空，空则说明匹配完毕
'''
class Solution(object):
    #这个函数非常关键，对应不同的右括号，要返回对应的左括号，观察其是否和
    #新来的右括号匹配
    def leftof(self,s):
        if s == ']':
            return '['
        if s == '}':
            return '{'
        return '('

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(','{','[']
        stack = []
        size = len(s)
        for i in range(size):
            temp = s[i]
            if temp in left:
                stack.append(temp)
            elif stack and self.leftof(temp) == stack[-1]:
                stack.pop()
            else:
                return False
        #观察栈是否为空，空则说明匹配完毕
        return not stack


if __name__ == '__main__':
    so = Solution()
    print(so.isValid("()"))
    print(so.isValid("()[]{}"))
    print(so.isValid("(]"))
    print(so.isValid("([)]"))
    print(so.isValid("{[]}"))