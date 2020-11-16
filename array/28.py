"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

"""


# class Solution:
# #     def strStr(self, haystack: str, needle: str) -> int:
# #         if len(needle) == 0:
# #             return 0
# #         hay_point = needle_point = 0
# #         while hay_point < len(haystack):
# #             if haystack[hay_point] == needle[needle_point]:
# #                 needle_point += 1
# #                 if needle_point == len(needle):
# #                     return hay_point - needle_point + 1
# #             elif needle_point > 0:
# #                 hay_point -= needle_point
# #                 needle_point = 0
# #
# #             hay_point += 1
# #
# #         return -1


# KMP 算法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        # 生成前缀表
        next = [0] * len_needle
        j = 0
        for i in range(1, len_needle):
            while j > 0 and needle[j] != needle[i]:
                j = next[j - 1]

            if needle[j] == needle[i]:
                j += 1
            next[i] = j
        print(next)
        hay_point = needle_point = 0
        while hay_point < len(haystack):
            while needle_point > 0 and haystack[hay_point] != needle[needle_point]:
                needle_point = next[needle_point - 1]
            if haystack[hay_point] == needle[needle_point]:
                needle_point += 1
                if needle_point == len_needle:
                    return hay_point - needle_point + 1

            hay_point += 1

        return -1


if __name__ == "__main__":
    solu = Solution()
    print(solu.strStr("aabaaabaaac", "aabaaac"))
