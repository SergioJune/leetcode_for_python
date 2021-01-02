"""
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
说明: N 是在 [0, 10^9] 范围内的一个整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/monotone-increasing-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        prev_num = 9
        res = 0
        step = 1
        while N != 0:
            remainder = N % 10

            if remainder > prev_num:
                remainder = remainder - 1
                res = step - 1

            res += step * remainder
            prev_num = remainder
            step *= 10
            N = N // 10

        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.monotoneIncreasingDigits(999998))
