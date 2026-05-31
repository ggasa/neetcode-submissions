class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums:
                output = [nums.index(diff),i]

            elif diff == num:
                output = [i,1]
            else:
                continue
        return output





