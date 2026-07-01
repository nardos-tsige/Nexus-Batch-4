class Solution:
    def isPalindrome(self, x: int) -> bool:
        nummy = str(x)

        if (str(x) == nummy[::-1]):
            return True
        return False
