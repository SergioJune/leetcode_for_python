"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 搞清楚什么时候需要计算结果和什么时候需要在栈中push或者pop即可
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        stack = []
        sign = 1
        num = 0
        modulus = 10
        for i in range(len(s)):
            ele = s[i]
            if ele.isdigit():
                num = num * modulus + int(ele)
            elif ele == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ele == ")":
                res += sign * num
                num = res
                sign = stack.pop()
                res = stack.pop()
            elif ele != " ":
                res += sign * num
                sign = -1 if ele == "-" else 1
                num = 0

        return res + sign * num