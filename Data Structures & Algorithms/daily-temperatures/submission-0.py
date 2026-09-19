class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)

        for idx, elt in enumerate(temperatures):
            while stk and (elt > stk[-1][0]):
                lastIdx = stk.pop()[1]
                res[lastIdx] = idx - lastIdx
            stk.append((elt, idx))
        return res