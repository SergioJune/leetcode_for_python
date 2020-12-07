"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 二分查找，第一次二分查找找出目标值，然后分开两部分，在分别在左右两部分找第一次和最后一次出现的值即可
class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        if len(nums) == 0:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        last_right = mid = first = last = -1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                if last == -1:
                    first = last = mid
                    last_right = right
                elif mid < first:
                    first = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        last_left = last +1
        while last_left <= last_right:
            mid = (last_left + last_right) >> 1
            if nums[mid] == target:
                if mid > last:
                    last = mid
                last_left = mid + 1
            elif nums[mid] > target:
                last_right = mid - 1
            else:
                last_left = mid + 1

        return [first, last]
