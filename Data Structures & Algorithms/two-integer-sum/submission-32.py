class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = list of integer
        # target = single integer
        seen = {}

        for i, num in enumerate(nums):
            rest = target-num
            if rest in seen:
                out = [seen[rest],i]
            seen[num] = i
        return out