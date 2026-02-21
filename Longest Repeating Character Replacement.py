class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = [0] * 26  
        max_count = 0
        result = 0
        
        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            counts[idx] += 1
            
            max_count = max(max_count, counts[idx])
            if (right - left + 1) - max_count > k:
                left_idx = ord(s[left]) - ord('A')
                counts[left_idx] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
