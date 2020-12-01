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


class Solution:
    def nextGreaterElements(self, nums: list) -> list:
        d = dict()
        max_value = -1
        res = [-1] * len(nums)
        for i in range(len(nums)):
            num = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > num:
                    res[i] = nums[j]
                    if d.get(num, None) is None:
                        d[num] = nums[j]
                    break
            else:
                val = d.get(num, -1)
                if val == -1 and max_value > num:
                    res[i] = max_value
                else:
                    res[i] = val
            if max_value < num:
                max_value = num

        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))
