from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        length = len(digits)
        for i in digits:
            length = length -1
            num = num + i*10**length
        return [int(i) for i in str(num)]