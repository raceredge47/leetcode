from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        median = (start+end)//2
        while True:
            if start == end == median:
                if nums[median] == target:
                    return median
                else:
                    return -1
            if nums[median] < target:
                start = median + 1
            else:
                end = median
            median = (start+end)//2