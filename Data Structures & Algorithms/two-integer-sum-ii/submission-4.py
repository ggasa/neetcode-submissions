class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx,num in enumerate(numbers):
            diff = target - num 
            if diff in numbers:
                idx_diff = numbers.index(diff)+1
            else:
                continue
            return [idx+1,idx_diff]
