class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numSet = set()

        left = 0
        longestLen = 0

        for right in range(len(s)):
            while s[right] in numSet:
                numSet.remove(s[left])
                left += 1
            numSet.add(s[right])
            longestLen = max(longestLen, right - left + 1)
        return longestLen
