"""

数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5


示例 2：

输入：[3,2]
输出：-1


示例 3：

输入：[2,2,1,1,1,2,2]
输出：2
"""

# 时间复杂度O(n) 空间复杂度 O(n)
# class Solution:
#     def majorityElement(self, nums: list) -> int:
#         m = dict()
#         for i in nums:
#             count = m.get(i, 0)
#             m[i] = count + 1
#
#         for k, v in m.items():
#             if v * 2 > len(nums):
#                 return k
#         return -1


# 时间复杂度O(n) 空间复杂度 O(1)  但是运行时间还是很垃圾
class Solution:
    def majorityElement(self, nums: list) -> int:
        res, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0:
                res, count = nums[i], 1
            else:
                if nums[i] == res:
                    count += 1
                else:
                    count -= 1

        t = len(nums) // 2 + 1
        if count > 0:
            cou = 0
            for num in nums:
                if num == res:
                    cou += 1
                    if cou == t:
                        return res

        return -1


if __name__ == "__main__":
    solu = Solution()
    print(solu.majorityElement([1, 2, 2, 1, 2]))
