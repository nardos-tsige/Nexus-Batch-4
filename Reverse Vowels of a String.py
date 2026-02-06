class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "AEIOUaeiou"
        vow = ''
        new_s = ''
        for i in s:
            if i in vowel:
                vow += i
        vow = vow[::-1]
        for i in s:
            if i not in vowel:
                new_s += i
            else:
                new_s += vow[0]
                vow = vow[1:]
        return new_s
