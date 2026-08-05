class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        prod = 1

        for i in range(len(nums)):
            prefix[i] = prod
            prod *= nums[i]
        
        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = prod
            prod *= nums[i]
        
        for i in range(len(nums)):
            prefix[i] *= suffix[i]
        
        return prefix
