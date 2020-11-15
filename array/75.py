"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

"""


# class Solution:
#     def sortColors(self, nums: list) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         d = {0: 0, 1: 0, 2: 0}
#         for n in nums:
#             d[n] = d[n] + 1
#         now = 0
#         for i in range(len(nums)):
#             while True:
#                 n = d[now]
#                 if n:
#                     d[now] -= 1
#                     break
#                 else:
#                     now += 1
#
#             nums[i] = now
#         print(nums)


class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, left, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = 0, nums[left]
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = 2, nums[right]
                right -= 1
                i -= 1

            i += 1
        print(nums)


if __name__ == "__main__":
    solu = Solution()
    solu.sortColors([0,1,0])