from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = sorted(list(set(nums))) 
        return n[-3] if len(n)>= 3 else n[-1]