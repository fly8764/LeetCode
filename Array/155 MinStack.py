# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
#相反的，还有最大栈
class MinStack1:
#根据定义做，超时
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        self.temp = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # 维持最小栈，从顶到底 递增
        while self.min and self.min[-1] < x:
            tmp = self.min.pop()
            self.temp.append(tmp)
        self.min.append(x)
        while self.temp:
            self.min.append(self.temp.pop())

    def pop(self) -> None:
        tmp = self.stack.pop()
        #把最小栈中的tmp删掉
        while self.min[-1] != tmp:
            self.temp.append(self.min.pop())
        self.min.pop()
        while self.temp:
            self.min.append(self.temp.pop())

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        #维持最小栈，和原始栈同步，每层只放置当前位置的最小元素
        #当新元素比当前辅助栈 栈顶元素还小的元素时，把新元素添加到
        #辅助栈的栈顶，否则重复防止辅助栈的栈顶元素
        if len(self.helper) == 0 or x < self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.helper.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[-1]


