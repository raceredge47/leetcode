from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        while k >= 1:
            if nums[k-1] == val:
                nums.pop(k-1)
            k = k - 1
        return len(nums)