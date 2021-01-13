"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def spiralOrder(self, matrix) -> list:
        if len(matrix) == 0:
            return []
        elif len(matrix) == 1:
            return matrix[0]

        res = []

        col_length = len(matrix[0])
        row_length = len(matrix)
        row = col = 0
        while True:
            for i in range(col, col_length):
                res.append(matrix[row][i])

            row += 1
            if row == row_length:
                break

            for i in range(row, row_length):
                res.append(matrix[i][col_length - 1])

            col_length -= 1
            if col_length == col:
                break

            for i in range(col_length - 1, col - 1, -1):
                res.append(matrix[row_length - 1][i])

            row_length -= 1
            if row_length == row:
                break

            for i in range(row_length - 1, row - 1, -1):
                res.append(matrix[i][col])

            col += 1
            if col == col_length:
                break

        return res



