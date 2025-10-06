class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l = len(columnTitle)
        if l == 1:
            return ord(columnTitle) - 64
        
        count = 0
        multi = 1
        for i in range(l, 0 , -1):
            if i == l:
                count += ord(columnTitle[i-1]) - 64
            else:
                multi *= 26
                count += multi * (ord(columnTitle[i-1]) - 64)
        return count