"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def fourSum(self, nums: list, target: int):
        last = []
        nums.sort()
        len_arr = len(nums)
        print(nums)
        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            if (nums[i] + nums[i+1] + nums[i+2] + nums[i+3]) > target:  # 剪枝：1、当前最小和 > target，结束“当前层循环”
                break
            if (nums[i] + nums[len_arr-1] + nums[len_arr-2] + nums[len_arr-3]) < target:# 2、当前最大和 < target，跳过“当前循环”
                continue

            for j in range(i+1, len(nums) - 2):
                if j != (i+1) and nums[j] == nums[j-1]:
                    continue
                if (nums[i] + nums[j] + nums[j + 1] + nums[j + 2]) > target:  # 剪枝：1、当前最小和 > target，结束“当前层循环”
                    break
                if (nums[i] + nums[j] + nums[len_arr - 1] + nums[len_arr - 2]) < target:  # 2、当前最大和 < target，跳过“当前循环”
                    continue
                left = j+1
                right = len(nums) - 1
                while left < right:
                    res = nums[i] + nums[j] + nums[left] + nums[right]
                    if res == target:
                        last.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif res > target:
                        right -= 1
                    else:
                        left += 1

        return last


if __name__ == "__main__":
    solu = Solution()
    print(solu.fourSum([0,4,-5,2,-2,4,2,-1,4], 12))
