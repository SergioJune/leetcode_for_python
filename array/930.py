"""
在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。

 

示例：

输入：A = [1,0,1,0,1], S = 2
输出：4
解释：
如下面黑体所示，有 4 个满足题目要求的子数组：
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-subarrays-with-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numSubarraysWithSum(self, A: list, S: int) -> int:
        left = right = 0
        res = 0
        while left < len(A):
            cur = 0
            while right < len(A):
                cur += A[right]
                right += 1
                if cur > S:
                    break
                if cur == S:
                    res += 1
            if A[right - 1] > S and left < (right-1):
                res += (right-left-1)*(right-left-2)//2
                left = right
            else:
                left += 1
                right = left

        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.numSubarraysWithSum([1,0,0,0,0,0,0,0,1], 0))
