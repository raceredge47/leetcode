class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rem = 0
        while x > 0:
            rem = rem*10 + x%10
            x = x//10
        return True if rem == num else False