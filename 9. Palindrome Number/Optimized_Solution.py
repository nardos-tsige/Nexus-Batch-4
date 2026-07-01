class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            nummy = 0
            num = x
            while x > 0:
                nummy = nummy * 10 + (x % 10)
                x = x // 10
            if nummy == num:
                return True
            else:
                return False
