class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictt = {')':'(', ']':'[','}':'{'}

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or stack.pop() != dictt[i]:
                    return False
        return not stack
