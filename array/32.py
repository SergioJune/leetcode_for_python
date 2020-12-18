"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i != "(":
                res = 0
                while len(stack) > 0:
                    if type(stack[-1]) == int:
                        res += stack.pop()
                    else:
                        break

                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                    if len(stack) > 0 and type(stack[-1]) == int:
                        res += 2 + stack.pop()
                    else:
                        res += 2
                    stack.append(res)
                    continue
                stack.append(res)

            stack.append(i)

        max_value = 0
        print(stack)
        for i in stack:
            if type(i) == int and max_value < i:
                max_value = i
        return max_value


if __name__ == "__main__":
    solu = Solution()
    print(solu.longestValidParentheses(")()())"))
