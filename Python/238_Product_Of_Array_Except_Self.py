from typing import List

class Solution:
    # This solution works fine with O(n) time and O(1) extra space complexity, yet question demands a solution without using division.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        ret = [0] * len(nums)
        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    ret[i] = product
        elif zero_count == 0:
            for i in range(len(nums)):
                ret[i] = int(product / nums[i])
        return ret
    """
    
def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, suff, ret = [0] * n, [0] * n, [0] * n
        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            ret[i] = pref[i] * suff[i]
        return ret