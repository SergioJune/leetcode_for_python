"""
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

 

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4
示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30
示例 3：

输入: piles = [30,11,23,4,20], H = 6
输出: 23
 

提示：

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/koko-eating-bananas
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math


class Solution:
    def minEatingSpeed(self, piles: list, H: int) -> int:
        # 首先获取堆数香蕉的最大值
        max_val = 0
        for i in piles:
            if max_val < i:
                max_val = i

        ans = 1
        # 速度在[1, max_val] 开始二分遍历
        left, right = 1, max_val
        while left <= right:
            mid = left + ((right - left) >> 1)
            # 遍历看看能不能吃完
            h = 0
            for i in piles:
                h += math.ceil(i / mid)
            if h <= H:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans