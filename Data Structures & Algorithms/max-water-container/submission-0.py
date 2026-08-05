class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr = 0
        lPtr = 0
        rPtr = len(heights) - 1

        while lPtr < rPtr:
            dist = rPtr - lPtr
            maxAr = max(maxAr, dist * min(heights[lPtr], heights[rPtr]))
            if heights[lPtr] < heights[rPtr]:
                lPtr += 1
            else:
                rPtr -= 1
        return maxAr