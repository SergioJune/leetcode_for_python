"""
给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。

 

示例 1：

输入：n = 5, start = 0
输出：8
解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
     "^" 为按位异或 XOR 运算符。

"""


# class Solution:
#     def xorOperation(self, n: int, start: int) -> int:
#         res = start
#         for i in range(2, 2*n, 2):
#             res ^= start + i
#         return res


class Solution:
    """
    1) 0 ^ x = x
    2) x ^ x = 0
    3) 2x ^ (2x+1) = 1
    """
    def xorOperation(self, n: int, start: int) -> int:
        res = 2 * self.xor(n, start // 2)  # 前面往右移了一位，所以后面需要移回来
        if n&1 and start&1:  # 都是奇数
            res += 1
        return res

    def xor(self, n, start):
        if start & 1:  # 奇数
            return (start - 1) ^ self.xor(n+1, start - 1)
        else:
            if n & 1:
                return start//2 + n - 1  # 就是最后以想，前面的都是 0
            else:
                return (n//2)&1


if __name__ == "__main__":
    solu = Solution()
    print(solu.xorOperation(5, 1))


