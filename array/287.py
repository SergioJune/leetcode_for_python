"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# class Solution:
# #     def findDuplicate(self, nums: list) -> int:
# #         nums.sort()
# #         last = 0
# #         for i in range(len(nums)):
# #             if last == nums[i]:
# #                 return last
# #             last = nums[i]


class Solution:
    def findDuplicate(self, nums: list) -> int:
        # 快慢指针，一个走两步，一个走一步
        low = nums[0]
        fast = nums[low]
        while fast != low:  # 相遇之后，快指针走2n步，慢指针走n步，其中 c为环周长，并且 n%c == 0
            low = nums[low]
            fast = nums[nums[fast]]

        # 接着继续找出环的起点，其中慢指针在环中位置为n-m，
        # 所以再走m步就是环的起始位置，所以另起一个指针从头开始，直到相遇就是m步
        walker = 0
        while walker != low:
            low = nums[low]
            walker = nums[walker]
        return walker


if __name__ == "__main__":
    solu = Solution()
    print(solu.findDuplicate([3,1,3,4,2]))