"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 使用递归 + 栈做
import math


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = "+"
        num = 0
        modulus = 10
        for i in range(len(s)):
            ele = s[i]
            if ele.isdigit():
                num = num * modulus + int(ele)

            if (not ele.isdigit() and ele != " ") or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(math.trunc(stack.pop() / num))

                sign = ele
                num = 0

        return sum(stack)
