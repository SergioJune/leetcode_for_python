"""
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:

输入: [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: [3,3,7,7,10,11,11]
输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-element-in-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def singleNonDuplicate(self, nums: list) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right-left)>>1)
            mid = mid-1 if mid&1 else mid
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid - 1

        return nums[left]
