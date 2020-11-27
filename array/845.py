"""
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。

 

示例 1：

输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
示例 2：

输入：[2,2,2]
输出：0
解释：不含 “山脉”。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-mountain-in-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestMountain(self, arr: list) -> int:
        if len(arr) < 3:
            return 0
        left, right, res = 0, 1, 0
        prev_num = arr[left]
        has_small = has_big = False
        while right < len(arr):
            if not has_big:  # 寻找最大值
                if arr[right] > prev_num:
                    has_small = True
                    prev_num = arr[right]
                elif arr[right] == prev_num:
                    has_small = False
                    left = right
                else:
                    if has_small:
                        has_big = True
                        has_small = False
                    else:
                        left = right
                    prev_num = arr[right]
            elif not has_small:  # 寻找最小值
                if arr[right] < prev_num:
                    prev_num = arr[right]
                else:
                    if (right - left) > res:
                        res = right - left
                    right -= 1
                    left = right
                    has_small = has_big = False

            right += 1

        if has_big:
            if (right - left) > res:
                res = right - left
        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.longestMountain([0,2,2]))
