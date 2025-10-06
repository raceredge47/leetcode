from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a = nums[0]
        for i in nums[1:]:
            a = a ^ i
        return a