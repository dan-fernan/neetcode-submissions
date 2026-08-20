class Solution:
    def isValid(self, s: str) -> bool:
        stk = [s[0]]

        for i in range(1, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stk.append(s[i])
            elif (len(stk) == 0): 
                return False
            elif (stk[-1] == '{' and s[i] == '}') or (stk[-1] == '(' and s[i] == ')') or (stk[-1] == '[' and s[i] == ']'):
                stk.pop()
            else:
                return False
        return len(stk) == 0
            

