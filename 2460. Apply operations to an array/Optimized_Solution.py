class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        #first applying n-1 operations
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        #shifting all zeros to the end using two-pointer
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                #swaping
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        
        return nums
