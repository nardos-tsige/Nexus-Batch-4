class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        if k == 1:
            return nums
        
        result = []
        deque_indices = deque()  
        
        for i in range(len(nums)):
        
            if deque_indices and deque_indices[0] <= i - k:
                deque_indices.popleft()
            
            while deque_indices and nums[deque_indices[-1]] < nums[i]:
                deque_indices.pop()
            
            deque_indices.append(i)
            if i >= k - 1:
                result.append(nums[deque_indices[0]]) 
        return result
