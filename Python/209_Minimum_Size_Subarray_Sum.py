from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0,0
        minL = len(nums) + 1
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                if r - l + 1 < minL:
                    minL = r - l + 1
                total -= nums[l]
                l += 1
        if minL == len(nums) + 1:
            return 0
        return minL
