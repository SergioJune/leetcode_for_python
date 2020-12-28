"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 我的方法：先循环一次第一个数组找出大于目标值的第一个位置，然后继续遍历其他的数组
# class Solution:
#     def findNumberIn2DArray(self, matrix, target: int) -> bool:
#         if len(matrix) == 0:
#             return False
#         right = len(matrix[0])-1
#         for i in range(len(matrix[0])):
#             if matrix[0][i] > target:
#                 right = i
#                 break
#         for nums in matrix:
#             left = 0
#             while left <= right:
#                 mid = left + ((right-left)>>1)
#                 if nums[mid] == target:
#                     return True
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return False


# 参考别人的方法
class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if len(matrix) == 0:
            return False
        length = len(matrix)
        left, right = 0, len(matrix[0]) - 1
        while left < length and right > -1:
            if matrix[left][right] == target:
                return True
            elif matrix[left][right] < target:
                left += 1
            else:
                right -= 1
        return False
