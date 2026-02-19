class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        
        for num in range(len(arr), 1, -1):
            idx = arr.index(num)
            
            if idx > 0:
                arr[:idx+1] = arr[:idx+1][::-1]
                result.append(idx + 1)

            arr[:num] = arr[:num][::-1]
            result.append(num)
        
        return result
