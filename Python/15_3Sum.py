class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = list()
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = len(nums) - 1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if sum < 0:
                    low += 1
                elif sum > 0:
                    high -= 1
                else:
                    ret.append([nums[i] , nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
        return ret