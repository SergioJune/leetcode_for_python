"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 自己实现快排来解决
# class Solution:
#     def findKthLargest(self, nums: list, k: int) -> int:
#
#         def inner_find(nums, left, pivot, k):
#
#             right = left
#             while right < pivot:
#                 if nums[right] < nums[pivot]:
#                     nums[left], nums[right] = nums[right], nums[left]
#                     left += 1
#                 right += 1
#
#             nums[left], nums[pivot] = nums[pivot], nums[left]
#             return left
#
#         k = len(nums) - k
#         left = 0
#         pivot = len(nums) - 1
#         while True:
#             left = inner_find(nums, left, pivot, k)
#             if left == k:
#                 return nums[left]
#             elif k > left:
#                 left += 1
#             else:
#                 pivot = left - 1
#                 left = 0


# 用系统的排序过
class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]