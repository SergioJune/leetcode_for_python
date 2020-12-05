"""
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# class Solution:
#     def nextGreaterElements(self, nums: list) -> list:
#         stack = []
#         max_stack = []
#         d = dict()
#         for num in nums:
#             while len(stack) > 0:
#                 if num > stack[-1]:
#                     eles = d.get(stack[-1], [])
#                     eles.append(num)
#                     d[stack[-1]] = eles
#                     stack.pop()
#                 else:
#                     break
#             stack.append(num)
#
#             if len(max_stack) == 0:
#                 max_stack.append(num)
#             else:
#                 if max_stack[-1] < num:
#                     max_stack.append(num)
#
#         # 需要清空 stack
#         i = 0
#         while len(stack) > 0:
#             val = stack.pop()
#             while i < len(max_stack) and max_stack[i] <= val:
#                 i += 1
#             eles = d.get(val, [])
#             if i == len(max_stack):
#                 eles.append(-1)
#             else:
#                 eles.append(max_stack[i])
#             d[val] = eles
#         res = [-1] * len(nums)
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] = d[nums[i]].pop()
#
#         return res


# 优化
class Solution:
    def nextGreaterElements(self, nums: list) -> list:
        res = [-1] * len(nums)
        stack = []
        for i in range(2 * len(nums) - 1, -1, -1):
            index = i % len(nums)
            while len(stack) > 0 and nums[index] >= nums[stack[-1]]:
                stack.pop()

            res[index] = -1 if len(stack) == 0 else nums[stack[-1]]
            stack.append(index)

        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))
