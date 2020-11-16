"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

 

说明：

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例：

输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出：[1,2,2,3,5,6]

"""


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right = m + n - 1
        first, secode = m - 1, n - 1
        while secode >= 0 and first >= 0:
            if nums1[first] >= nums2[secode]:
                nums1[right] = nums1[first]
                first -= 1
            else:
                nums1[right] = nums2[secode]
                secode -= 1
            right -= 1
        for i in range(secode, -1, -1):
            nums1[right] = nums2[i]
            right -= 1
        print(nums1)


if __name__ == "__main__":
    solu = Solution()
    solu.merge([4,5,6,0,0,0], 3, [1,2,3], 3)