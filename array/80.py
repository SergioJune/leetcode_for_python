"""
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 你不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 你不需要考虑数组中超出新长度后面的元素。

"""


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        len_nums = len(nums)
        if len_nums < 2:
            return len_nums
        left, right, start_index = 0, 1, 0
        while right < len_nums:
            if nums[left] != nums[right]:
                left += 1
                start_index = right
                nums[left] = nums[right]
            elif nums[left] == nums[right] and (right - start_index) < 2:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1


if __name__ == "__main__":
    solu = Solution()
    print(solu.removeDuplicates([1,1,1,2,2,3]))
