class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        arr = []
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                arr.append(word1[i])
                i += 1
            else:
                arr.append(word2[j])
                j += 1
        arr.append(word1[i:])
        arr.append(word2[j:])
        
        return ''.join(arr)
