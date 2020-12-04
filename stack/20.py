"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) == 0:
#             return True
#         queue = []
#         for symbol in s:
#             if symbol == "(" or symbol == "[" or symbol == "{":
#                 queue.append(symbol)
#             else:
#                 if len(queue) == 0:
#                     return False
#                 ele = queue.pop()
#                 if abs(ord(symbol) - ord(ele)) > 2:
#                     return False
#
#         if len(queue) > 0:
#             return False
#         return True


class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "(": ")",
            "[": "]",
            "{": "}",
            "?": "?"
        }
        queue = ['?']
        for symbol in s:
            if symbol in d:
                queue.append(symbol)
            else:
                if d.get(queue.pop(), None) == symbol:
                    continue
                return False

        return len(queue) == 1
