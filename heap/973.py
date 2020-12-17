"""
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

 

示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释：
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）
 

提示：

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-closest-points-to-origin
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def kClosest(self, points: list, K: int) -> list:
        if len(points) == 0:
            return []
        res = [points[0]]
        for i in range(1, K):
            self.insert(res, points[i])

        max_val = res[0][0] ** 2 + res[0][1] ** 2
        for i in range(K, len(points)):
            val = points[i][0] ** 2 + points[i][1] ** 2
            if max_val > val:
                self.update(res, points[i], val)
                max_val = res[0][0] ** 2 + res[0][1] ** 2

        return res

    def update(self, heap, point, val):
        heap[0] = point
        index = 0
        while True:
            left = index * 2 + 1
            right = left + 1
            if left >= len(heap):
                break
            left_val = heap[left][0] ** 2 + heap[left][1] ** 2
            if right < len(heap):
                right_val = heap[right][0] ** 2 + heap[right][1] ** 2
            else:
                right_val = None
            if val >= left_val and (right_val is None or (right_val and val >= right_val)):
                break
            if right_val is None or left_val >= right_val:
                heap[index], heap[left] = heap[left], heap[index]
                index = left
            else:
                heap[index], heap[right] = heap[right], heap[index]
                index = right

    def insert(self, heap, val):
        heap.append(val)
        self.heapity(heap)

    def heapity(self, heap):
        index = len(heap) - 1
        son_val = heap[index][0] ** 2 + heap[index][1] ** 2
        while index > 0:
            parent = (index - 1) // 2
            par_val = heap[parent][0] ** 2 + heap[parent][1] ** 2
            if son_val > par_val:
                heap[index], heap[parent] = heap[parent], heap[index]
                index = parent
            else:
                break


if __name__ == "__main__":
    solu = Solution()
    print(solu.kClosest([[-66,42],[-67,94],[46,10],[35,27],[-9,-6],[-84,-97],[38,-22],[3,-39],[71,-97],[-40,-86],[-45,56],[-91,59],[24,-11],[91,100],[-68,43],[34,27]], 6))