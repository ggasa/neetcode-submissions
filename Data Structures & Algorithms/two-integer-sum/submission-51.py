class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}

        for i,num in enumerate(nums):
            dif = target - num
            if dif in h_map.keys():
                i_dif = h_map[dif]
                return [i_dif,i]
            else:
                h_map[num] = i
                continue
            
        return [i_dif, i]
                
