class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
       
        first_word = words[0]
        result = []
        for char in set(first_word):
            
            min_occurrences = first_word.count(char)
            for word in words[1:]:
                current_count = word.count(char)
               
                if current_count == 0:
                    min_occurrences = 0
                    break
                min_occurrences = min(min_occurrences, current_count)

            result.extend([char] * min_occurrences)
        
        return result
