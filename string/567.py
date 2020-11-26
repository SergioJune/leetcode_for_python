"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
 

示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = dict()
        for i in s1:
            d[i] = d.get(i, 0) + 1
        left, right = 0, 0
        match = False
        while right < len(s2):
            if d.get(s2[right], 0) > 0:
                d[s2[right]] -= 1
                match = True
                right += 1
            elif match:
                if (right - left) == len(s1):
                    return True
                if left < right:
                    d[s2[left]] += 1
                else:
                    right += 1
                    match = False
                left += 1
            else:
                left += 1
                right = left

        if (right - left) == len(s1):
            return True
        return False
