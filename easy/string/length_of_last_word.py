class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split(" ")
        word = [word for word in word_list if word]
        return len(word[-1])