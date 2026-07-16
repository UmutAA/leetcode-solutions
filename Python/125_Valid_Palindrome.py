class Solution:
    #This solution works fine, yet it works with O(n) time and extra space complexity
    """
    def isPalindrome(self, s: str) -> bool:
        filtered_str = "".join([char for char in s if char.isalphanum()])
        filtered = filtered_str.lower()
        return filtered_str == filtered_str[::-1]
    """
    #This one works also fine, plus it works with O(n) time and O(1) extra space complexity
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True