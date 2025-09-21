class Solution:
    def __init__(self):
        self.memo = {}   # storage for already computed results

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if n in self.memo:          # if already computed, just reuse it
            return self.memo[n]

        # otherwise compute and store it
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]