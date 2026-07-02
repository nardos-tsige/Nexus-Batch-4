class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #sorting
        sorted_nums = sorted(nums)
        
        #create a dictionary mapping each number to 
        #how many numbers are smaller than it
        smaller_count = {}
        for i, num in enumerate(sorted_nums):
            #only store the first occurrence(smallest index)
            if num not in smaller_count:
                smaller_count[num] = i  #i = how many elements before it
        #build the answer using the dictionary
        return [smaller_count[num] for num in nums]

  #time complexity - O(n log n)
