"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        nums = []
        for i in s:
            n = ord(i)
            if 47 < n < 58:
                nums.append(n)
            elif 64 < n < 91:
                nums.append(n)
            elif 96 < n < 123:
                nums.append(n-32)

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
                continue
            return False
        return True


if __name__ == "__main__":
    solu = Solution()
    print(solu.isPalindrome("Zeus was deified, saw Suez."))
