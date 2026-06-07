class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math

        new_list = []
        for i,num in enumerate(nums):
            temp = nums.pop(i)
            tot = math.prod(nums)
            new_list.append(tot)

            nums.insert(i,temp)

        return new_list