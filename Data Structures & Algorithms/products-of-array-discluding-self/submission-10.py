class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        length = len(nums)
        output = [1]*length
        #left only
        for i,num in enumerate(nums):
            output[i] *= prefix
            prefix *= num
        
        #right only
        for i in range((length-1),-1,-1):
            output[i] *= suffix
            suffix *= nums[i]
        
        
        return output