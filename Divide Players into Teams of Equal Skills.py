class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        
        left, right = 0, n - 1
        target_sum = skill[left] + skill[right]
        total = 0
        
        while left < right:
            current_sum = skill[left] + skill[right]
            
            if current_sum != target_sum:
                return -1
            
            total += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return total
