class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        x = []
        count = 0
        for j in nums:
            if j > 0:
                x.append(j)
            if j == 0:
                count += 1
        k = 0
        while k < count:
            x.append(0)
            k += 1
        return x
