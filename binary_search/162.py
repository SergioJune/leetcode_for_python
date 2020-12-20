"""
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是 O(logN) 时间复杂度的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 我的写法
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + ((right-left)>>1)
#             right_val = -sys.maxsize-1 if mid+1 >= len(nums) else nums[mid+1]
#             left_val = -sys.maxsize-1 if mid-1 < 0 else nums[mid-1]
#             if nums[mid] > right_val and nums[mid] > left_val:
#                 return mid
#             elif nums[mid] <= right_val:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return left


class Solution:
    def findPeakElement(self, nums: list) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left