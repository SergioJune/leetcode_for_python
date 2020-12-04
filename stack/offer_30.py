"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sort_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.sort_stack) == 0:
            self.sort_stack.append(x)
        else:
            if self.sort_stack[-1] >= x:
                self.sort_stack.append(x)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.sort_stack[-1]:
            self.sort_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.sort_stack[-1]