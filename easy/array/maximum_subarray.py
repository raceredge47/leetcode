from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = float('-inf')
        sum = 0
        for i in nums:
            # if sum == 0:
            #     max = i
            
            sum += i
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max