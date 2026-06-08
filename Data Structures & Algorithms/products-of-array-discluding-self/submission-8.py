class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        output = []
        length = len(nums)

        #left only
        for num in nums:
            output.append(prefix)
            prefix *= num
        
        #right only
        for i in range((length-1),-1,-1):
            output[i] *= suffix
            suffix *= nums[i]


        
        return output