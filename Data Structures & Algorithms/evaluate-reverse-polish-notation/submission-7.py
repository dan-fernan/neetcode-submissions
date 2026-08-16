class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token == "+":
                secondElt = stk.pop()
                firstElt = stk.pop()
                stk.append(firstElt + secondElt)
            elif token == '-':
                secondElt = stk.pop()
                firstElt = stk.pop()
                stk.append(firstElt - secondElt)
            elif token == '*':
                secondElt = stk.pop()
                firstElt = stk.pop()
                stk.append(firstElt * secondElt)
            elif token == '/':
                secondElt = stk.pop()
                firstElt = stk.pop()
                stk.append(int(firstElt / secondElt))
            else:
                stk.append(int(token))
        
        return int(stk[0])

            