"""
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

 

示例 1:

输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:

输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
示例 3：

输入：houses = [1,5], heaters = [2]
输出：3
 

提示：

1 <= houses.length, heaters.length <= 3 * 104
1 <= houses[i], heaters[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/heaters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# class Solution:
#     def findRadius(self, houses: list, heaters: list) -> int:
#         res = 0
#         heaters.sort()
#         for h in houses:
#             dis = self.findClosestDistance(h, heaters)
#             res = max(res, dis)
#         return res
#
#     # 二分搜索，找出每个房子与暖炉最近的距离
#     def findClosestDistance(self, pos, heaters):
#         if pos <= heaters[0]:
#             return heaters[0] - pos
#         if pos >= heaters[len(heaters) - 1]:
#             return pos - heaters[len(heaters) - 1]
#
#         left, right = 0, len(heaters) - 1
#         while left <= right:
#             mid = left + ((right - left) >> 1)
#             if heaters[mid] == pos:
#                 return 0
#             elif heaters[mid] > pos:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#
#         if pos - heaters[right] > heaters[left] - pos:
#             return heaters[left] - pos
#         return pos - heaters[right]


# 更简便的方法  直接击败百分百
# 思路，这个需要将两个参数排序，然后不需要每次都进行二分搜索，只需要每次寻找第一个大于这个房子的坐标即可，然后对比前后的距离找出最小值
# 最后再获取每个房子距离暖炉的最大值
class Solution:
    def findRadius(self, houses: list, heaters: list) -> int:
        houses.sort()
        heaters = [float("-inf")] + sorted(heaters) + [float('inf')]
        pos = res = 0
        for h in houses:
            while h > heaters[pos]:
                pos += 1
            dis = min(heaters[pos]-h, h-heaters[pos-1])
            res = max(dis, res)
        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.findRadius([1,2,3], [1,2,3]))
