from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        k = len(nums)
        while k >= 1:
            if nums[k-1] in s:
                nums.pop(k-1)
            s.add(nums[k-1])
            k = k -1
        return len(nums)
       