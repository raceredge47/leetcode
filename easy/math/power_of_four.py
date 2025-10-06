class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            n=n**1/4
        return True if n==1 else False
    