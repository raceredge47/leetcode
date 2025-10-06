from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        p = 0
        for sp in prices[1:]:
            if sp < bp:
                bp = sp
                continue

            max = sp - bp
            if max > p:
                p = max
        return p
        