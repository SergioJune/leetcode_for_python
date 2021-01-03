"""
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

 

示例：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-labels
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 我自己的做法
# class Solution:
#     def partitionLabels(self, S: str) -> list:
#         if len(S) < 2:
#             return [len(S)]
#         d = dict()
#         num = 0
#         right = 0
#         while right < len(S):
#             val = d.get(S[right], None)
#             if val is None:
#                 d[S[right]] = num
#                 num += 1
#             else:
#                 for k in d:
#                     if d[k] > val:
#                         d[k] = val
#                 num = val + 1
#             right += 1
#         res = [0] * num
#         for i in S:
#             res[d[i]] += 1
#
#         return res


class Solution:
    def partitionLabels(self, S: str) -> list:
        d = dict()
        for i in range(len(S)):
            d[S[i]] = i

        left = right = 0
        res = []
        for i in range(len(S)):
            right = max(right, d[S[i]])
            if i == right:
                res.append(right-left+1)
                left = i + 1
        return res

if __name__ == "__main__":
    solu = Solution()
    print(solu.partitionLabels("ababcbacadefegdehijhklij"))
