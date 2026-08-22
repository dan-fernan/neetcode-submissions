class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        minimumK = right

        while left <= right:
            mid = (left + right) // 2

            n = sum(math.ceil(pile/mid) for pile in piles)

            if n <= h:
                minimumK = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return minimumK
            


        
