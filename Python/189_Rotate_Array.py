from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #O(n) space and time
        """
        n = len(nums)
        temp = [0] * n
        for i in range(n):
            temp[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = temp[i]
        """

        #O(n) time O(1) space
        n = len(nums)
        k %= n
        def reverse(l: int, r: int) -> None:
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
                
            

        