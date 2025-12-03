class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = n
        while i >= n:
            if i % 2 == 0:
                break
            else:
                i *= 2
        return i
