class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_unique = len(set(nums))
        len_original = len(nums)
        if len_unique < len_original:
            output = True
        else:
            output = False
        
        return output