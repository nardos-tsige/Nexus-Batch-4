class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        k = []
        for ch in set(words[0]): 
            min_count = float('inf')

            for word in words:
                min_count = min(min_count, word.count(ch))

            k.extend([ch] * min_count)

        return k
