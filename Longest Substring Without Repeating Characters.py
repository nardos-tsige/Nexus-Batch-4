class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        check = set()
        max_len = 0
        for i in range(len(s)):
            while s[i] in check:
                check.remove(s[left])
                left += 1

            check.add(s[i])
            max_len = max(max_len, i - left + 1)
        return max_len
