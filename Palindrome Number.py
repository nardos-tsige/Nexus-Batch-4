class Solution:
    def isPalindrome(self, x: int) -> bool:
        rem, ana = 0, x
        if ana < 0:
            return False
        while ana > 0:
            s = ana % 10
            rem = (rem * 10) + s
            ana = ana // 10
        if rem == x:
            return True
        return False
