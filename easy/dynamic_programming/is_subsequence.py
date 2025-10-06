class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        temp = ''
        count = 0
        for i in range(t_len):
            if count < s_len and s[count] == t[i]:
                temp += t[i]
                count += 1
        return True if temp == s else False