class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = defaultdict(list)

        for string in strs:
            arrCnt = [0] * 26

            for i in range(len(string)):
                arrCnt[ord(string[i]) - 97] += 1
            key = '#'.join([str(x) for x in arrCnt])
            d[key].append(string)
        
        for arr in d.values():
            res.append(arr)
        return res
        
