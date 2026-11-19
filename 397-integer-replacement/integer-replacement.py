class Solution:
    def __init__(self):
        self.results = {1: 0}

    def integerReplacement(self, n: int) -> int:
        if n not in self.results:
            if n % 2:  # n odd
                self.results[n] = 1 + min(
                    self.integerReplacement(n + 1),
                    self.integerReplacement(n - 1)
                )
            else:
                self.results[n] = 1 + self.integerReplacement(n / 2)

        return self.results[n]
