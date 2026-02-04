class Solution:
    def similarPairs(self, words: List[str]) -> int:
        arr = []
        for word in words:
            new_word = sorted(set(word))
            arr.append(new_word)

        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    count += 1

        return count
