class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        
        for target in range(n, 0, -1):
            index = arr.index(target)

            if index == target - 1:
                continue
            if index != 0:
                
                self.flip(arr, index + 1)
                result.append(index + 1)
            self.flip(arr, target)
            result.append(target)
        
        return result
    
    def flip(self, arr: List[int], k: int) -> None:
        left, right = 0, k - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
