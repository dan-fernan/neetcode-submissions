class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {num:idx for idx, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            compl = target - num
            if compl in numsDict.keys() and numsDict[compl] != idx:
                return [numsDict[compl], idx] if idx > numsDict[compl] else [idx, numsDict[compl]]
        
        return [-1]
        