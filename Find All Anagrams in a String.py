class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr = []
        ps = sorted (p)
        len_p = len(p)
        for i in range(len(s) - len_p + 1):
            window = s[i : i + len_p]
            if sorted(window) == ps:
                arr.append(i)
        return arr
