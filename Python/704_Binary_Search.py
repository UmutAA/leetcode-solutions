from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            i = low + ((high - low) // 2)
            if nums[i] < target:
                low = i + 1
            elif nums[i] > target:
                high = i - 1
            else:
                return i
        return -1