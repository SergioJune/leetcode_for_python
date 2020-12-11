"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def generateParenthesis(self, n: int) -> list:
        d = dict()

        def inner_gen(n):
            if n == 0:
                return []
            if n == 1:
                return ["()"]

            other = d.get(n - 1, None)
            if other is None:
                other = inner_gen(n - 1)
                d[n - 1] = other
            res = [i + "()" for i in other]
            res.pop()
            res += ["(" + i + ")" for i in other]
            res += ["()" + i for i in other]
            count = 2
            while count < n:

                one = d.get(count, None)
                if one is None:
                    one = inner_gen(count)
                    d[count] = one
                two = d.get(n - count, None)
                if two is None:
                    two = inner_gen(n - count)
                    d[n - count] = two
                for i in one:
                    res += [i + j for j in two]

                count += 1
            d[n] = res
            return list(set(res))

        return inner_gen(n)


if __name__ == "__main__":
    solu = Solution()
    print(solu.generateParenthesis(3))
