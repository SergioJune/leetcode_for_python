"""
递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

示例1:

 输入：A = 1, B = 10
 输出：10
示例2:

 输入：A = 3, B = 4
 输出：12
提示:

保证乘法范围不会溢出

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recursive-mulitply-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 单纯的加法运算
# class Solution:
#     def multiply(self, A: int, B: int) -> int:
#
#         def inner_mult(a, b):
#             if a == 0:
#                 return 0
#
#             return b + inner_mult(a - 1, b)
#
#         if A > B:
#             return inner_mult(B, A)
#         return inner_mult(A, B)


# 利用移位
class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A == 1:
            return B
        if A % 2 == 0:
            return self.multiply(A >> 1, B << 1)

        return B + self.multiply(A >> 1, B << 1)
