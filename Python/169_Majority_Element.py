class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #This solution works in O(n) time and space complexity
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num,cnt in counts.items():
            if cnt > len(nums) // 2:
                return num
        """
        #For the follow-up Boyer-Moore Voting Algorithm is used:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate