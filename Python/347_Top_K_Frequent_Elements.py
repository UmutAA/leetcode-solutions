from typing import List
from collections import defaultdict

class Solution:
    #This solution works fine but time complexisty is O(nlogn).
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        arr = list()
        for num, cnt in freq.items():
            arr.append([cnt,num])
        arr.sort()
        ret = list()
        while len(ret) < k:
            ret.append(arr.pop()[1])
        return ret
    """
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freqs = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] += 1

        for num,cnt in count.items():
            freqs[cnt].append(num)
        ret = list()
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret