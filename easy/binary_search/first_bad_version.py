# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        median = (start+end)//2

        while True:
            bad = isBadVersion(median)
            if start == median == end:
                return median
            if bad:
                end = median
            else:
                start = median + 1
            median = (start+end)//2