class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ''
        for i in s.split(' ')[::-1]:
            if i:
                temp += i + ' '
        return temp.strip()