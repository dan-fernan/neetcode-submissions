class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
        return False
       
       charCnt = [0] * 26

       for i in range(len(s)):
        charCnt[ord(s[i]) - ord('a')] += 1
        charCnt[ord(t[i]) - ord('a')] -= 1

       return all(cnt == 0 for cnt in charCnt)

