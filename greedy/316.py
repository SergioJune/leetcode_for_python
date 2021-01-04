"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 104
s 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = dict()
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1

        stack = []
        seed = set()
        for i in s:
            if i not in seed:
                while stack and i < stack[-1] and d[stack[-1]] > 0:
                    seed.discard(stack.pop())
                seed.add(i)
                stack.append(i)
            d[i] -= 1
        return "".join(stack)


if __name__ == "__main__":
    solu = Solution()
    print(solu.removeDuplicateLetters("cdadabcc"))
