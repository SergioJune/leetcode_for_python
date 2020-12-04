"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

 

示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
示例 3：

输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/backspace-string-compare
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 双指针解法
# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         left, right = len(S) - 1, len(T) - 1
#         while left > -1 or right > -1:
#             if left > -1 and S[left] == "#":
#                 other_left = left
#                 while left > -1 and other_left >= left:
#                     if S[other_left] == "#":
#                         left -= 2
#                     other_left -= 1
#
#             if right > -1 and T[right] == "#":
#                 other_right = right
#                 while right > -1 and other_right >= right:
#                     if T[other_right] == "#":
#                         right -= 2
#                     other_right -= 1
#
#             if left < 0 and right < 0:
#                 return True
#             elif left < 0:
#                 return False
#             elif right < 0:
#                 return False
#             if S[left] != T[right]:
#                 return False
#             left -= 1
#             right -= 1
#
#         return True


# 栈解法
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        left_queue = self.operat_str(S)
        right_queue = self.operat_str(T)

        while len(left_queue) > 0 and len(right_queue) > 0:
            if left_queue.pop() != right_queue.pop():
                return False
        return len(right_queue) == len(left_queue)

    def operat_str(self, s):
        queue = []
        for i in s:
            if i == "#":
                if len(queue) > 0:
                    queue.pop()
            else:
                queue.append(i)
        return queue