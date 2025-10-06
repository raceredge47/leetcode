class Solution:
    def fib(self, n: int) -> int:
        last_one = 0
        current = 1
        for i in range(n+1):
            if i == 0:
                current = 0
                continue
            if i == 1:
                current = 1
                continue
            a = current
            current += last_one
            last_one = a
        return current