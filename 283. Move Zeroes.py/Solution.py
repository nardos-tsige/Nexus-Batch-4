class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.remove(nums[i])

        for j in range(count):
            nums.append(0)
        return nums
