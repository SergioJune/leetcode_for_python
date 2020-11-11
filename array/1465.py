"""
矩形蛋糕的高度为 h 且宽度为 w，给你两个整数数组 horizontalCuts 和 verticalCuts，其中 horizontalCuts[i] 是从矩形蛋糕顶部到第  i 个水平切口的距离，类似地， verticalCuts[j] 是从矩形蛋糕的左侧到第 j 个竖直切口的距离。

请你按数组 horizontalCuts 和 verticalCuts 中提供的水平和竖直位置切割后，请你找出 面积最大 的那份蛋糕，并返回其 面积 。由于答案可能是一个很大的数字，因此需要将结果对 10^9 + 7 取余后返回。

输入：h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
输出：4
解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色的那份蛋糕面积最大。

"""


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list, verticalCuts: list) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()

        M, N = len(horizontalCuts), len(verticalCuts)
        max_h = max_v = 0
        for i in range(M - 1):
            max_h = max(max_h, horizontalCuts[i+1] - horizontalCuts[i])
        for i in range(N - 1):
            max_v = max(max_v, verticalCuts[i+1] - verticalCuts[i])

        return max_h * max_v % (10**9 + 7)


if __name__ == "__main__":
    solu = Solution()
    print(solu.maxArea(5, 4, [1, 2, 4], [1, 3]))
