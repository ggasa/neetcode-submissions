class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num in num_dict.keys():
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        print(num_dict)
        for num in num_dict.values():
            if num < 2:
                continue 
            else:
                return True
        return False
            