class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if nums has target, then it should reutrn the index,
        # if not, it should return -1

        # how to impelement the binary search?
        
        pointer_1 = 0
        pointer_mid = len(nums)//2
        pointer_2 = len(nums)-1
        
        
        output =-1
        
        while pointer_1 <= pointer_2:
            pointer_mid = (pointer_1+pointer_2)//2
            if target == nums[pointer_mid]:
                return pointer_mid
            elif target > nums[pointer_mid]:
                pointer_1 = pointer_mid+1
            else:
                pointer_2 = pointer_mid-1

        return output

