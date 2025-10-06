class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        if x >= 1 and x <= 3:
            return 1

        c = 0
        for i in range(2, int(x/2)+1):
            multi = i * i
            if multi == x:
                return i
            if multi < x:
                c = i
                continue
            if multi > x:
                break
        return c
        