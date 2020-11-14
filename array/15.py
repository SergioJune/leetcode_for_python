"""

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution:
    def threeSum(self, nums: list) -> list:
        res = []
        len_arr = len(nums)
        nums.sort()
        print(nums)
        for i in range(len_arr - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1
                right = len_arr - 1
                while left < right:
                    val = nums[i] + nums[left] + nums[right]
                    if val == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif val > 0:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.threeSum([-1,0,1,2,-1,-4]))
    print()
    print(solu.threeSum([0,0,0,0]))
    print()
    print(solu.threeSum([-1,0,1,0]))
