class Solution:
    def similarPairs(self, words: List[str]) -> int:
        seen = {}
        count = 0

        for word in words:
            key = "".join(sorted(set(word)))

            if key in seen:
                count += seen[key]
                seen[key] += 1
            else:
                seen[key] = 1

        return count
