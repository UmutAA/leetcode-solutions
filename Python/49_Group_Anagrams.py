from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            words[sortedS].append(s)
        return list(words.values())