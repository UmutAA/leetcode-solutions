class Solution:
    def mySqrt(self, x: int) -> int:
        l,r,y = 0,x,0

        while l <= r:
            m = l + (r - l) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                y = m
            else:
                return m
        return y