"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

"""


# class Solution:
#     def removeDuplicates(self, nums: list) -> int:
#         arr_len = len(nums)
#         if arr_len <= 1:
#             return arr_len
#         left, right, num = 1, 1, nums[0] + 1
#         while right < arr_len:
#             if nums[right] >= num:
#                 nums[left] = nums[right]
#                 num = nums[left] + 1
#                 left += 1
#                 right += 1
#             else:
#                 right += 1
#
#         return left


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        arr_len = len(nums)
        if arr_len <= 1:
            return arr_len
        left, right = 0, 1
        while right < arr_len:
            if (nums[right] - nums[left]) > 0:
                nums[left + 1] = nums[right]
                left += 1

            right += 1
        print(nums)
        return left + 1


if __name__ == "__main__":
    solu = Solution()
    print(solu.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

