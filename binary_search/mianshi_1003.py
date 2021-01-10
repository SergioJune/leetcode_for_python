"""
搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。

示例1:

 输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
 输出: 8（元素5在该数组中的索引）
示例2:

 输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
 输出：-1 （没有找到）
提示:

arr 长度范围在[1, 1000000]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-rotate-array-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def search(self, arr: list, target: int) -> int:

        def inner_search(arr, left, right, target):
            while left < right:
                mid = left + ((right-left)>>1)
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if arr[left] == target else -1

        left, right = 0, len(arr)-1
        while left < right:
            mid = left + ((right-left)>>1)
            if arr[mid] > arr[right]:
                right = mid
            elif arr[mid] == arr[right]:
                right -= 1
            else:
                left = mid + 1
        print(left)
        if arr[0] < target:
            return inner_search(arr, 0, left, target)
        return inner_search(arr, left+1, len(arr)-1,  target)


if __name__ == "__main__":
    solu = Solution()
    print(solu.search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5))