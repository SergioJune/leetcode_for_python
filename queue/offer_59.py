"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if k == 1:
            return nums
        if len(nums) == 0:
            return nums
        max_queue = []
        res = []
        n = 0
        for i in range(len(nums)):
            num = nums[i]
            while len(max_queue) > 0 and max_queue[-1] < num:
                max_queue.pop()

            max_queue.append(num)
            n += 1

            if n == k:
                res.append(max_queue[0])
                if nums[i - k + 1] == max_queue[0]:
                    max_queue.pop(0)
                n -= 1

        return res
