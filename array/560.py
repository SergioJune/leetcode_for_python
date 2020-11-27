"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        left = res = 0
        right = 1
        sum_num = nums[0]
        while left < len(nums):
            if sum_num < k:
                if len(nums) == right:
                    if len(nums) - 1 == left:
                        break
                    left += 1
                    sum_num = 0
                    right = left
                sum_num += nums[right]
                right += 1
            else:
                if sum_num == k:
                    res += 1
                sum_num -= nums[left]
                left += 1
                if left == right:
                    if len(nums) == right:
                        break
                    sum_num = nums[left]
                    right = left + 1
        else:
            if sum_num == k:
                res += 1

        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.subarraySum([1,-1,0], 0))
