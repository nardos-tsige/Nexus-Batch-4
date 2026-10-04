class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        new_s = []
        j = 0
        for i, c in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                new_s.append(' ')
                j += 1              
            new_s.append(c)

        return ''.join(new_s)
