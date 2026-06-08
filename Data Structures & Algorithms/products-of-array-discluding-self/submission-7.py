class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        output = [] 
        
        #left pass
        for i,num in enumerate(nums):
            output.append(prefix)
            prefix *= num  

        #right pass
        print(output)
        for i in range((len(nums)-1),-1,-1):
            print(i)
            output[i] *= suffix
            suffix *= nums[i]
            
        return output