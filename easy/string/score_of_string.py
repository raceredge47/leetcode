class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0
        l = len(s)
        for i in range(1, l):
            count += abs(ord(s[i-1]) - ord(s[i]))
        return count
        