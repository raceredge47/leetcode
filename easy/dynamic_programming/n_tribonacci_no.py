class Solution:
    def tribonacci(self, n: int) -> int:
        last_one = 1
        last_second = 0
        current = 1
        for i in range(n+1):
            if i == 0:
                current = 0
                continue
            if i == 1 or i == 2:
                current = 1
                continue
            a = last_one
            b = current
            current += last_one + last_second
            last_one = b
            last_second = a
        return current