"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        if not words:
            return []
        w_len, s_len = len(words[0]), len(s)
        t_len = w_len * len(words)  # 子串的长度

        word_dict = {}  # words的哈希表
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

        ans = []
        for offset in range(w_len):
            lo, lo_max = offset, s_len - t_len
            while lo <= lo_max:
                tmp_dict = word_dict.copy()
                match = True
                for hi in range(lo + t_len, lo, -w_len):    # 从尾到头搜索单词
                    word = s[hi - w_len: hi]
                    if word not in tmp_dict or tmp_dict.get(word, 0) == 0:
                        match = False
                        break   # 当前单词不符合要求 直接停止这个子串的搜索
                    tmp_dict[word] -= 1
                if match:
                    ans.append(lo)
                lo = hi     # 对lo直接赋值 这就是相比法二优化的地方
        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.findSubstring("barfoothefoobarman", ["foo","bar"]))
