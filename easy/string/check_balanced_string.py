class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = 0
        even = 0
        for i, n in enumerate(num):
            if i % 2 == 0:
                even += int(n)
            else:
                odd += int(n)
        return True if odd == even else False