# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        median = (start+end)//2

        while True:
            res = guess(median)
            if res == -1:
                end = median
            elif res == 1:
                start = median + 1
            elif res == 0:
                return median
            median = (start+end)//2