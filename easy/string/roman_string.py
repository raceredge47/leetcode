class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        num = []
        for index, i in enumerate(s, 0):
            num.append(roman[i])
            if index != 0 and num[index-1] < num[index]:
                num[index-1] = -(num[index-1])
        return sum(num)
