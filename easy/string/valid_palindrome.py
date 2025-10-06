class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for i in s:
            if i.isalnum():
                t += i.lower()
        return True if t == t[::-1] else False
        