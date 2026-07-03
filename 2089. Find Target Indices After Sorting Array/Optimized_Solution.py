class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less_count = 0
        count = 0
        
        for num in nums:
            if num < target:
                less_count += 1
            elif num == target:
                count += 1
        
        return list(range(less_count, less_count + count)) 
#Time complexity - O(n)
