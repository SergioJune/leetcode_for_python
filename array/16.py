"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。


示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import sys

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        len_nums = len(nums)
        near_value, near_res = sys.maxsize, target
        for i in range(len_nums - 2):
            left, right = i+1, len_nums - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if abs(target-res) < near_value:
                    near_value = abs(target-res)
                    near_res = res
                if target == res:  # 这步很关键，少了这步，至少需要循环多很多次
                    return res
                elif target > res:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:  # 这里的循环都是去掉重复元素
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return near_res


if __name__ == "__main__":
    solu = Solution()
    print(solu.threeSumClosest([0, 1, 2], 0))
