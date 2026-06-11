class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        output = [1]*len(nums)

        for i,num in enumerate(nums):
            # for the prefix
            output[i] *= prefix
            prefix *= num 

            #for the suffix
            output[~i] *= suffix
            suffix *= nums[~i]
        return output
    