class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        pickedstr = strs[0]
        for i, letter in enumerate(pickedstr):
            for str in strs[1:len(strs)]:
                if i > len(str) - 1 or letter != str[i]:
                    return s
            s += letter
        return s
