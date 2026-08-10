class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(s.split(' ')).lower()
        print(string)

        left = 0
        right = len(string) - 1

        while left < right:
            if not string[left].isalnum():
                left += 1
                continue
            if not string[right].isalnum():
                right -= 1
                continue
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        
        return True