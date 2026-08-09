class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        maxLen = 0

        for num in n:
            if num - 1 not in n:
                length = 0
                while num + length in n:
                    length += 1
                    maxLen = max(length, maxLen)
        return maxLen