"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

 

示例 1：

输入："hello"
输出："holle"
示例 2：

输入："leetcode"
输出："leotcede"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) < 2:
            return s
        yuan = {
            "a": 1,
            "e": 1,
            "i": 1,
            "o": 1,
            "u": 1,
            "A": 1,
            "E": 1,
            "I": 1,
            "O": 1,
            "U": 1,
        }

        len_str = len(s)
        res = [""] * len_str
        left, right = 0, len_str - 1
        while left <= right:
            if not yuan.get(s[left], None):
                res[left] = s[left]
                left += 1
                continue
            if not yuan.get(s[right]):
                res[right] = s[right]
                right -= 1
                continue

            res[left], res[right] = s[right], s[left]

            left += 1
            right -= 1
        return "".join(res)