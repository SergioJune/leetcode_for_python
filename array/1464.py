class Solution:
    def maxProduct(self, nums) -> int:
        max1 = max2 = 0
        for i in range(len(nums)):
            if nums[i] >= max1:
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max2 = nums[i]
        return (max1 - 1) * (max2 - 1)


if __name__ == "__main__":
    solu = Solution()
    print(solu.maxProduct([10,2,5,2]))
