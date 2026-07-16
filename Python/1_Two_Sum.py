from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()
        for i,num in enumerate(nums):
            diff = target - num
            if diff in indices and indices[diff] != i:
                return [indices[diff], i]
            else:
                indices[num] = i
        return []