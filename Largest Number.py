class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        str_nums = [str(num) for num in nums]
    
        n = len(str_nums)
        for i in range(n):
            for j in range(i+1, n):

                if str_nums[i] + str_nums[j] < str_nums[j] + str_nums[i]:
                 
                    str_nums[i], str_nums[j] = str_nums[j], str_nums[i]
        
    
        result = ''.join(str_nums)
        if result[0] == '0':
            return '0'
        else:
            return result
