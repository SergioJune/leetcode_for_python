"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# class Solution:
#     def minArray(self, numbers: list) -> int:
#         min_val = numbers[0]
#         left, right = 0, len(numbers) - 1
#         while left <= right:
#             mid = left + ((right - left) >> 1)
#             if numbers[mid] == min_val:
#                 left += 1
#             elif numbers[mid] < min_val:
#                 min_val = numbers[mid]
#                 right = mid - 1
#             else:
#                 left = mid + 1
#
#             if left < len(numbers) and min_val > numbers[left]:
#                 min_val = numbers[left]
#
#         return min_val


class Solution:
    def minArray(self, numbers: list) -> int:
        left, right = 0, len(numbers)-1
        while left < right:
            mid = left + ((right-left) >> 1)
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1

        return numbers[left]
