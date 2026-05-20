class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for i,num in enumerate(nums):
            rest = target - num
            if rest in memory:
                out = [memory[rest],i]
            else:
                memory[num] = i
        return out