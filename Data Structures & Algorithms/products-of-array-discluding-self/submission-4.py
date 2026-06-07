class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        #left pass
        suffix = 1
        output = [] 
        output2 = []  
        for i,num in enumerate(nums):
            output.append(prefix)
            prefix *= num        
        #right pass
        for i,num in enumerate(nums):
            output2.append(suffix)
            suffix *= nums[-(i+1)]
        output2.reverse()
        print(output)
        print(output2)
        result = [x * y for x, y in zip(output, output2)]

        return result